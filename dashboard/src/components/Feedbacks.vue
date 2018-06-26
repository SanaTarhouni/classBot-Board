  <template >
  <div>
  <b-card no-body class="mb-1" v-for="item in feeds" :key='item.fellow'>
            <b-card-header header-tag="header" class="p-1" role="tab">
                <b-btn block href="#" v-b-toggle.accordion1 variant="info">{{item.fellow}}</b-btn>
            </b-card-header>
            <b-collapse id="accordion1" visible accordion="my-accordion" role="tabpanel">
                <b-card-body>
                    <p class="card-text">
                        {{ item.text }}
                    </p>
                </b-card-body>
            </b-collapse>
    </b-card>
  </div>
  </template>
<script>
export default { 
  name: 'c-feeds',
  props: {  
    feeds: {
      type: Array
    }
 
  }
}
</script>
