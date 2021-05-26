import axios from '@/utils/http'

export function getList(params) {
  return axios({
    url: '/parse/hots',
    method: 'get',
    params
  })
}
export function getHotsChange(params) {
  return axios({
    url: '/parse/hotschange',
    method: 'get',
    params,
  })
}
