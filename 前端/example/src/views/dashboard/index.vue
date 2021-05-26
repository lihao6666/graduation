<template>
  <div class="app-container">
    <el-table
      v-loading="listLoading"
      :data="list"
      element-loading-text="Loading"
      border
      fit
      highlight-current-row
      :row-class-name="tableRowClassName"
    >
      <el-table-column align="center" label="排行" width="95">
        <template slot-scope="scope">
          {{ scope.row.ranking }}
        </template>
      </el-table-column>
      <el-table-column label="内容">
        <template slot-scope="scope">
          {{ scope.row.content }}
        </template>
      </el-table-column>
      <el-table-column label="热度" width="110" align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.count }}</span>
        </template>
      </el-table-column>
      <!-- <el-table-column label="描述" width="110" align="center">
        <template slot-scope="scope">
          {{ scope.row.pageviews }}
        </template>
      </el-table-column> -->
      <el-table-column class-name="status-col" label="描述" width="110" align="center">
        <template slot-scope="scope">
          <el-tag :type="scope.row.desc | statusFilter" >{{ scope.row.desc }}</el-tag>
        </template>
      </el-table-column>

      <!-- <el-table-column align="center" prop="created_at" label="Display_time" width="200">
        <template slot-scope="scope">
          <i class="el-icon-time" />
          <span>{{ scope.row.display_time }}</span>
        </template>
      </el-table-column> -->
    </el-table>
    <pagination v-show="total>0"
      :total="total"
      :page.sync="page"
      :limit.sync="limit"
      :dataList="templist"
      @pagination="getPaginationData"
      @updateDataList="updateDataList"
    />
  </div>
</template>

<script>
import { getList } from '@/api/hots'
import Pagination from '@/components/Pagination'

export default {
  components: { Pagination },
  filters: {
    statusFilter(status) {
      const statusMap = {
        热: 'danger',
        新: 'primary',
        荐: 'success',
        None: 'info'
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      list: null,
      templist: null,
      listOrigin: null,
      listLoading: true,
      total: 0,
      page: 1000,
      limit: 10,
      listQuery: {
        hot_type: 'weibo',
      },
    }
  },
  created() {
    this.fetchData()
  },
  methods: {
    fetchData() {
      this.listLoading = true
      getList(this.listQuery).then(response => {
        // console.log(response)
        
        this.listOrigin = response.data.fields.hots
        this.templist = [...this.listOrigin]
        this.page = 1
        this.total = 50
        this.listLoading = false
      })
    },
    tableRowClassName (row) {
      if (parseInt(row.row.ranking) <= 5) {
        return 'rowstyle';
      }
    },
    getPaginationData (val) {
      this.templist = [...this.listOrigin]
      this.limit = val.limit
    },
    updateDataList (list) {
      this.list = list
    }
  }
}
</script>


<style lang="scss">
.el-tag {
  width: 60px;
}
.el-table .rowstyle {
  color: red;
}
</style>
