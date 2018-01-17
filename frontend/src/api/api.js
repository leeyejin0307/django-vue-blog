import axios from 'axios'
import * as Cookies from 'js-cookie'

const baseUrl = "http://localhost:8000/api/v1/"

// 文章列表
export const articleList = (page, order, search) => {
  return axios.get(`${baseUrl}posts/?page=${page}${order}${search}`)
}

// 文章详情
export const articleDetail = params => {
  return axios.get(`${baseUrl}posts/${params}/`)
}

// 评论列表
export const commentList = params => {
  return axios.get(`${baseUrl}comments/?search=${params}`)
}

// 种类列表
export const categoryList = () => {
  return axios.get(`${baseUrl}categorys/`)
}

// 用户登陆
export const login = params => {
  return axios.post(`${baseUrl}login/`, params)
}
