
const state = {
  content: null,
  patch: null,
  res: null,
}
const mutations = {
  ADD_CONTENT: (state,param) => {
      state.content = param.content
      state.patch = param.patch 
  },
  ADD_RES: (state, param) => {
    state.res = param
  },
}
// const actions = {
//   toggleSideBar({ commit }) {
//     commit('TOGGLE_SIDEBAR')
//   },
//   closeSideBar({ commit }, { withoutAnimation }) {
//     commit('CLOSE_SIDEBAR', withoutAnimation)
//   },
//   toggleDevice({ commit }, device) {
//     commit('TOGGLE_DEVICE', device)
//   }
// }

export default {
  namespaced: true,
  state,
  mutations,
}
