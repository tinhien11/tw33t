import Vue from 'vue'
import App from './App'
import router from './router'
import '../node_modules/semantic-ui-css/semantic.css'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
