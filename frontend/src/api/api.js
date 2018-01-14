import axios from 'axios'
import * as Cookies from 'js-cookie'

const baseUrl = "http://localhost:8000/api/v1/"

// 文章列表
export const articleList = params => {
  return axios.get(`${baseUrl}posts/?page=${params}`)
}

// 文章详情
export const articleDetail = params => {
  return axios.get(`${baseUrl}posts/${params}/`)
}

// 评论列表
export const commentList = params => {
  return axios.get(`${baseUrl}comments/?search=${params}`)
}
