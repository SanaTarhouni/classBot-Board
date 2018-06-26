<template>
  <div class="sidebar">
    <SidebarHeader/>
    <SidebarForm/>
    <nav class="sidebar-nav">
      <div slot="header"></div>
      <ul class="nav">
          <template >
            <sidebar-nav-dropdown :name="'Excellence camp'" :class="''" :icon="'icon-speedometer'" />
          </template>
        <template   v-for="(item, index) in navItems">
            <SidebarNavItem v-show="item.excellenceCamp" :key="index" :classes="item.class">
                <SidebarNavLink :name="item.name" :url="'/module/'+item.ClassroomID" :icon="item.icon" :badge="item.badge" :variant="item.variant"/>
            </SidebarNavItem>
        </template>
          <template >
            <sidebar-nav-dropdown  :name="'Technical camp'" :class="''" :icon="'icon-speedometer'"/>
          </template>
        <template  v-for="(item, index) in navItems">
            <SidebarNavItem  v-show="!item.excellenceCamp" :key="index" :classes="item.class">
                <SidebarNavLink  :name="item.name" :url="'/module/'+item.ClassroomID" :icon="item.icon" :badge="item.badge" :variant="item.variant"/>
              </SidebarNavItem>
        </template>

      </ul>
      <slot></slot>
    </nav>
    <SidebarFooter/>
    <SidebarMinimizer/>
  </div>
</template>
<script>
import SidebarFooter from './SidebarFooter'
import SidebarForm from './SidebarForm'
import SidebarHeader from './SidebarHeader'
import SidebarMinimizer from './SidebarMinimizer'
import SidebarNavDivider from './SidebarNavDivider'
import SidebarNavDropdown from './SidebarNavDropdown'
import SidebarNavLink from './SidebarNavLink'
import SidebarNavTitle from './SidebarNavTitle'
import SidebarNavItem from './SidebarNavItem'
import SidebarNavLabel from './SidebarNavLabel'
import api from '@/services/api'

export default {
  name: 'sidebar',
 data() {
   return {
     navItems : []


 }},
  components: {
    SidebarFooter,
    SidebarForm,
    SidebarHeader,
    SidebarMinimizer,
    SidebarNavDivider,
    SidebarNavDropdown,
    SidebarNavLink,
    SidebarNavTitle,
    SidebarNavItem,
    SidebarNavLabel
  },
  methods: {
    handleClick (e) {
      e.preventDefault()
      e.target.parentElement.classList.toggle('open')
    }
  },
  created() {
    api().get("modules").then(response => {
      this.navItems=response.data
      console.log(this.navItems)
    })

  }

}
</script>

<style scoped lang="css">
.nav-link {
  cursor: pointer;
}
.sidebar {
  width:25%;
}
.sidebar .nav {
  width:100%;
}
.sidebar-nav {
  width:100%;
}
</style>
