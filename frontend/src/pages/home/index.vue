<template>
  <div class="">
    <galHd></galHd>
    <main>
      <div class="inner">
        <!-- POSTLIST BEGIN -->
        <section class="main-left">

          <!-- POSTLIST HEADER -->
          <div class="post-filter">
            <a href="#">最新</a>
            <a href="#">热门</a>
            <a href="#">
              <icon name="rss" scale="0.8"></icon>
              RSS订阅
            </a>
          </div>

          <!-- POSTLIST MAIN -->
          <div v-if="articles && articles.length">
            <article class="post-list" v-for="(art, index) of articles">
              <div class="post-list-header">
                <span>{{ art.author }}</span>
                <span>{{ art.updated|moment }}</span>
              </div>
              <h2 class="post-list-title">
                <router-link :to="`/post/${art.id}/`">
                  {{ art.title }}
                </router-link>
              </h2>
              <div class="post-list-body">
                {{ art.body }}
              </div>
              <div class="post-list-footer">
                <span>
                  <icon name="eye" scale="0.8"></icon>
                  {{ art.views }}
                </span>
                <span>
                  <icon name="comments" scale="0.8"></icon>
                  {{ art.comment_count }}
                </span>
              </div>
            </article>
          </div>

          <div v-if="!(articles && articles.length)">
            还没有文章发布!
          </div>

        </section>
        <!-- POSTLIST END -->
      </div>
    </main>
    <galFt></galFt>
  </div>
</template>

<script>
import '../../filter/moment.js'
import galHd from '../../components/header'
import galFt from '../../components/footer'
import { articleList } from '../../api/api'
export default {
  components: {
    galHd,
    galFt,
  },
  data () {
    return {
      articles: [],
    }
  },
  created () {
    // 获取文章列表
    articleList()
    .then( res => {
      this.articles = res.data.results
    })
  }
}
</script>

<style scoped>
@import '../../assets/css/home.css';
</style>
