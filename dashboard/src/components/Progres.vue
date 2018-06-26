<template>
<div>
<pulse-loader :color="color" :loading="loading" ></pulse-loader>
<div v-show="!loading">

     <b-row>
      <b-col md="6" class="my-1">
        <b-form-group horizontal label="Filter" class="mb-0">
          <b-input-group>
            <b-form-input v-model="filter" placeholder="Type to Search" />
            <b-input-group-append>
              <b-btn :disabled="!filter" @click="filter = ''">Clear</b-btn>
            </b-input-group-append>
          </b-input-group>
        </b-form-group>
      </b-col>
      <b-col md="6" class="my-1">
        <b-form-group horizontal label="Sort" class="mb-0">
          <b-input-group>
            <b-form-select v-model="sortBy" :options="sortOptions">
              <option slot="first" :value="null">-- none --</option>
            </b-form-select>
          </b-input-group>
        </b-form-group>
      </b-col>
      <b-col md="6" class="my-1">
          <b-form-group horizontal label="Per page" class="mb-0">
          <b-form-select :options="pageOptions"  v-model="perPage" />
        </b-form-group>
      </b-col>

    </b-row>
    <b-table class="mb-0 table-outline" responsive="sm" hover 
    :items="tableItems" :fields="tableFields"  
    head-variant="light"
    :current-page="currentPage"
             :per-page="perPage"
             :filter="filter"
             :sort-by.sync="sortBy"
             :sort-desc.sync="sortDesc"
             :sort-direction="sortDirection"
             @filtered="onFiltered">
            
            <div slot="avatar" class="avatar" slot-scope="item">
              <img :src="item.value.url" class="img-avatar" alt="">
              <span class="avatar-status" v-bind:class="{ 'bg-success': item.value.status == 'finished',  'bg-warning': item.value.status == 'InProgress', 'bg-danger': item.value.status == 'outOfDeadline', 'bg-secondary': item.value.status == '' }"></span>
            </div>
            <div slot="fellow" slot-scope="item">
              <div>{{item.value.name}}</div>
              <div class="small text-muted">
                <span>
                  cohort 2
                </span> 
              </div>
            </div>
            <div slot="progress" slot-scope="item">
              <div class="clearfix">
                <div class="float-left">
                  <strong >{{Math.ceil(item.value.value)}} %</strong>

                </div>
                <div class="float-right">
                  <small class="text-muted">{{item.value.period}}</small>
                </div>
              </div>
              <b-progress height={} class="progress-xs" v-model="item.value.value" :variant="variant(item.value.value)"></b-progress>
            </div>   
          <div slot="Status" slot-scope="item">
          <b-badge :variant="getBadge(item.value.value)"> {{item.value.value}} </b-badge>
           </div>
            <div slot="Deadline" slot-scope="item">
              <strong>{{item.value}}</strong>
            </div>
          </b-table>
        <b-row>
      <b-col md="6" class="my-1">
        <b-pagination :total-rows="totalRows" :per-page="perPage" v-model="currentPage" class="my-0" />
      </b-col>
    </b-row>
</div>
</div>
</template>

<script>

import api from '@/services/api.js'
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'

export default {
  name: 'c-progres',
  components: {PulseLoader},
  methods: {
    variant(value) {
      let $variant;
      if (value <= 25) {
        $variant = 'danger';
      } else if (value > 25 && value <= 50) {
        $variant = 'warning';
      } else if (value > 50 && value < 100) {
        $variant = 'info';
      } else if (value=100) {
        $variant = 'success';
      }
      return $variant;
    },
    getBadge(status) {
      return status === 'Inprogress'
        ? 'warning'
        : status === 'finished'
          ? 'success'
          : status === 'NotStarted' ? 'danger' : 'primary';
    },
    onFiltered(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },
    loadFellows(module_id) {
      this.loading = true
    api().post('module/progress',{"module_id": parseInt(module_id)})
    .then(response => {
  
       this.tableItems=response.data
       this.loading = false
    })
    .catch(e => {
    
      console.log(e)
      this.errors.push(e)
    })

    }
  }, 
  data() {
    return {
      sortBy: null,
      sortDesc: false,
      color : "#00cec9",
      sortDirection: 'asc',
      filter: null,
      loading : true,
      currentPage: 1,
      pageOptions: [5, 10, 15],
      perPage : 5,
      module_id : this.$route.params.module_id,
      tableItems: [],
      tableFields: {
        avatar: {
          label: '<i class="icon-people"></i>',
          class: 'text-center'
        },
        fellow: {
          label: 'Fellow',
          sortable: true
        },
        progress: {
          label: 'Progress',
          sortable: true
        },
        Deadline: {
          label: 'Deadline',
          class: 'text-center',
          sortable: true
        },
        // TODO
        // status should be a calculated field : fx(progress)
        Status: {
          label: 'Status',
          sortable: true
        }
      }
    };
  },
  computed: {
    sortOptions() {
      // Create an options list from our fields
      return [
        { text: 'Fellow', value: 'Fellow' },
        { text: 'Progress', value: 'Progress' },
        { text: 'Deadline', value: 'Deadline' },
        { text: 'Status', value: 'Status' }
      ];
    }
  },
  mounted() {
    this.loadFellows(this.module_id)
 
  },
    beforeRouteUpdate(to,from, next){
      this.loadFellows(to.params.module_id)
      next()
  }
}
</script>
<style scoped>

.v-spinner{
      margin: auto;
    width: 10%;
}
</style>
