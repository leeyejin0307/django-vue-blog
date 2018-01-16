import Vue from 'vue'
import Router from 'vue-router'

import Home from '../pages/home/index'
import PostDetail from '../pages/postdetail/index'
import Category from '../pages/category/index'

Vue.use(Router)

export default new Router({
  routes: [
    {
      /** 首页 **/
      path: '/',
      name: 'Home',
      component: Home,
      meta: {
        title: '首页 - Blog'
      }
    },
    {
      /** 文章详情页 **/
      path: '/post/:id/',
      name: 'PostDetail',
      component: PostDetail,
    },
    {
      /** 文章分类页 **/
      path: '/categorys/',
      name: 'Category',
      component: Category,
    },
  ]
})
