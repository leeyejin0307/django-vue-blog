import axios from 'axios'
import * as Cookies from 'js-cookie'

const baseUrl = "http://localhost:8000/api/v1/"

// 文章列表
export const articleList = () => {
  return axios.get(`${baseUrl}posts/`)
}
