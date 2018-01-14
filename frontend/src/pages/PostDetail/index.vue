<template lang="html">
  <div class="">
    <galHd></galHd>
    <main>
      <div class="inner">
        <!-- POST DETAIL BEGIN -->
        <section class="main-left">
          <h1 class="post-title">{{ article.title }}</h1>
          <div class="post-header">
            <span>{{ article.created|moment }}</span>
            <span>{{ article.views }} 阅读</span>
            <span>{{ article.comment_count }} 评论</span>
          </div>
          <div class="post-body">
            <vue-markdown :source="article.body">
            </vue-markdown>
          </div>
          <div class="post-comment">
            <section v-if="!(comments && comments.length)">还没有评论!</section>
            <section v-for="(comment, index) of comments">
              <span>{{ comment.author }}</span>
              <span>{{ comment.created|moment }}</span>
              <p>{{ comment.content }}</p>
            </section>
          </div>
        </section>
        <!-- POST DETAIL END -->
      </div>
    </main>
    <galFt></galFt>
  </div>
</template>

<script>
import VueMarkdown from 'vue-markdown'

import '../../filter/moment.js'
import galHd from '../../components/header'
import galFt from '../../components/footer'
import { articleDetail, commentList } from '../../api/api'
export default {
  components: {
    galHd,
    galFt,
    VueMarkdown,
  },
  data () {
    return {
      article: [],
      comments: [],
    }
  },
  created () {
    // 获取文章列表
    articleDetail(this.$route.params.id)
    .then( res => {
      this.article = res.data
    })
    // 获取评论列表
    commentList(this.$route.params.id)
    .then( res => {
      this.comments = res.data.results
    })
  }
}

</script>

<style scoped>
@import '../../assets/css/github-markdown.css';
@import '../../assets/css/post_detail.css';
</style>
