<template>
  <div class="animated fadeIn">
    <b-row>
      <b-col sm="6" lg="3">
        <b-card>
          <div class="h4 m-0">{{excelence}}</div>
          <div>Excelence modules</div>

        </b-card>
      </b-col>
        <b-col sm="6" lg="3">
        <b-card>
          <div class="h4 m-0">{{technical}}</div>
          <div>Technical modules</div>

        </b-card>
      </b-col>
      <b-col sm="6" lg="3">
        <b-card>
          <div class="h4 m-0">{{users}}</div>
          <div>Fellows</div>

        </b-card>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import api from '@/services/api'
export default {
  name: 'widgets',
  data () {
    return {
      technical : 11,
      excelence : 4,
      users: 28,
      msg: 'Widgets'
    }


  },
  methods : {
    loadfellows() {

    }
  },
  mounted () {
    this.loadfellows()
  }
}
</script>
