/*
 * @Author: zep
 * @LastEditors: zep
 * @Description: file content
 */
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './plugins/element.js'
import * as echarts from 'echarts'

import axios from './utils/http'
import utils from './assets/js/utils'
import constants from './assets/js/constants'

import '@/styles/index.scss'
import 'element-ui/lib/theme-chalk/index.css'


Vue.prototype.$utils = utils
Vue.prototype.$constants = constants
Vue.prototype.$http = axios
Vue.prototype.$echarts = echarts

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
