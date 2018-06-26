import Vue from 'vue'
import Router from 'vue-router'

// Containers
import Full from '@/containers/Full'

// Viimpoews
import Dashboard from '@/views/Dashboard'
import Progres from '@/components/Progres'

Vue.use(Router)

export default new Router({
  mode: 'hash',
  linkActiveClass: 'open active',
  scrollBehavior: () => ({ y: 0 }),
  routes: [
    {
      path: '/',
      redirect: '/dashboard',
      name: 'Home',
      component: Full,
      children: [
        {
          path: 'dashboard/',
          name: 'Dashboard',
          component: Dashboard
        },
        {
          path: 'module/:module_id',
          name: 'Module',
          component: Progres
        }

      ]
    }
  ]
})
