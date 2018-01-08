import Vue from 'vue'
import App from './App'
import router from './router'

Vue.config.productionTip = false

/** ICON LIB BEGIN **/
import 'vue-awesome/icons'
import Icon from 'vue-awesome/components/Icon'
Vue.component('icon', Icon)
/** ICON LIB END **/

new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
