import axios from '@/utils/http'

export function updateRequest(data) {
  return axios({
    url: '/config/request',
    method: 'post',
    data
  })
}
export function getConfigs(params) {
    return axios({
      url: '/config/request',
      method: 'get',
      params
    })
  }