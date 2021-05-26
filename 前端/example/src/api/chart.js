import axios from '@/utils/http'

export function getSearch(params) {
  return axios({
    url: '/parse/search',
    method: 'get',
    params
  })
}
export function addSearch(params) {
  return axios({
    url: '/parse/addsearch',
    method: 'get',
    params
  })
}

export function getDetail(params) {
    return axios({
      url: '/parse/detail',
      method: 'get',
      params,
    })
  }
  export function getDetailChange(params) {
    return axios({
      url: '/parse/detailchange',
      method: 'get',
      params,
    })
  }
