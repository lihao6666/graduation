import Vue from 'vue'
import Router from 'vue-router'


Vue.use(Router)
import Layout from '@/layout'

export const constantRoutes = [
  {
    path: '/',
    component: Layout,
    redirect: '/hots',
  },
  {
  path: '/hots',
  component: Layout,
  redirect: '/hots/weibo',
  name: 'hots',
  meta: {
    title: '热点排行',
    icon: 'el-icon-s-help'
  },
  children: [{
      path: 'weibo',
      name: 'weibo',
      component: () => import('@/views/hots/weibo'),
      meta: {
        title: '微博',
        icon: 'el-icon-reading'
      }
    },
    {
      path: 'hotchart',
      name: 'hotChart',
      hidden: true,
      component: () => import('@/views/hots/chart'),
      meta: {
        title: '趋势',
        icon: 'el-icon-reading'
      },
    },
    {
      path: 'zhihu',
      name: 'zhihu',
      component: () => import('@/views/hots/zhihu'),
      meta: {
        title: '知乎',
        icon: 'el-icon-reading'
      }
    }
  ]
},



  {
    path: '/dashboard',
    component: Layout,
    redirect: '/dashboard/weibo',
    name: 'dashboard',
    meta: {
      title: 'Dashboard',
      icon: 'el-icon-s-data'
    },
    children: [{
        path: 'weibo',
        name: 'weibo_analyse',
        component: () => import('@/views/dashboard/weibo/index'),
        meta: {
          title: '微博',
          icon: 'el-icon-reading'
        },
      },
      {
        path: 'detail',
        name: 'detail',
        hidden: true,
        component: () => import('@/views/detail/weibo'),
        meta: {
          title: '详情',
          icon: 'el-icon-reading'
        },
      },
      {
        path: 'zhihu',
        name: 'zhihu_analyse',
        component: () => import('@/views/dashboard/index'),
        meta: {
          title: '知乎',
          icon: 'el-icon-reading'
        }
      }
    ]
  },

  {
    path: '/setting',
    component: Layout,
    children: [
      {
        path: 'index',
        component: () => import('@/views/setting/index'),
        name: 'setting',
        meta: { title: '设置', icon: 'el-icon-setting', affix: true }
      }
    ]
  },
]

// const router = new VueRouter({
//   // mode: 'history',
//   base: process.env.BASE_URL,
//   routes
// })
const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({
    y: 0
  }),
  routes: constantRoutes
})

const router = createRouter()

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}
export default router