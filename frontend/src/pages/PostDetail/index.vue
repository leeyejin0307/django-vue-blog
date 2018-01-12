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
            <p>{{ article.body }}</p>
          </div>
          <div class="post-comment">
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
  </div>
</template>

<script>
import '../../filter/moment.js'
import galHd from '../../components/header'
import { articleDetail, commentList } from '../../api/api'
export default {
  components: {
    galHd,
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
      console.log(this.comments)
    })
  }
}

</script>

<style scoped>
@import '../../assets/css/post_detail.css';
</style>
