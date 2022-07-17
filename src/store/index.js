import { createStore } from 'vuex'

export default createStore({
  state: {
    isLoading: false,
    isAthenticated: false,
    token:''
  },
  getters: {
  },
  mutations: {
    initializeStore (state){
      if(localStorage.getItem('token')) {
        state.token=localStorage.getItem('token')
        state.isAthenticated=true
      }
      else{
        state.token=''
        state.isAthenticated=false
      }
    },
    setIsLoading(state, status){
      state.isLoading=status
    },
    setToken(state,token){
      state.token=token
      state.isAthenticated=true
    },
    removeToken(state){
      state.token=''
      state.isAthenticated=false
    }
  },
  actions: {
  },
  modules: {
  }
})
