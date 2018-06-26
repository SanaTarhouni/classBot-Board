<template>
  <aside class="aside-menu">
 <b-card header-tag="header" footer-tag="footer">
              <div slot="header" style="text-align:center">
        <i class="fa fa-comments"></i> <div ><strong> Fellows Feedbacks</strong></div>
        </div>
     <div role="tablist">
      <c-feeds :feeds="feeds" />
        </div>
       </b-card>
  </aside>
</template>

<script>

import cFeeds from '@/components/Feedbacks'
export default {
  name: 'c-aside',
  components:{cFeeds},
  data(){ return {
     feeds: [
    {fellow: 'sana', text: 'feed1'},
    {fellow: 'Amine', text: 'feed2'},
    {fellow: 'Manel', text: 'feed3'}
  ]

  }}
}
</script>
