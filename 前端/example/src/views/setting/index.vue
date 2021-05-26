<template>
  <div class="app-container">
    <el-table
      v-loading="listLoading"
      :data="list"
      border
      fit
      highlight-current-row
      style="width: 100%"
    >
      <el-table-column align="center" label="序号" width="80">
        <template slot-scope="scope">
          <span>{{ scope.$index + 1 }}</span>
        </template>
      </el-table-column>

      <el-table-column width="70px" align="center" label="类型">
        <template slot-scope="{ row }">
          <span>{{ row.fields.parse_type }}</span>
        </template>
      </el-table-column>

      <el-table-column show-overflow-tooltip align="center" label="headers">
        <template slot-scope="{ row }">
          <span>{{ row.fields.headers }}</span>
        </template>
      </el-table-column>

      <el-table-column show-overflow-tooltip align="center" label="cookies">
        <template slot-scope="{ row }">
          <span>{{ row.fields.cookies }}</span>
        </template>
      </el-table-column>

      <el-table-column class-name="status-col" label="状态" width="110">
        <template slot-scope="{ row }">
          <el-tag :type="row.fields.status | statusFilter">
            {{ row.fields.status }}
          </el-tag>
        </template>
      </el-table-column>

      <el-table-column align="center" label="Actions" width="120">
        <template slot-scope="{ row }">
          <el-button
            type="primary"
            size="small"
            icon="el-icon-edit"
            :disabled='row.fields.status == "可用"'
            @click="editConfig(row)"
            >编辑
          </el-button>
        </template>
      </el-table-column>
    </el-table>
    <el-dialog title="编辑" :visible.sync="configVisible">
      <el-form
        ref="dataForm"
        :model="temp"
        label-position="left"
        label-width="70px"
        style="width: 400px; margin-left: 50px"
      >
        <el-form-item label="类型">
          <el-input v-model="temp.parse_type" :disabled="true" />
        </el-form-item>
        <el-form-item label="headers">
          <el-input v-model="temp.headers" type="textarea" />
        </el-form-item>
        <el-form-item label="cookies">
          <el-input v-model="temp.cookies" type="textarea" />
        </el-form-item>
        <el-form-item label="status">
          <el-tag
            v-model="temp.status"
            :type="temp.status | statusFilter"
          >{{ temp.status }}</el-tag>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="configVisible = false"> 取消 </el-button>
        <el-button type="primary" @click="updateConfig"> 更新 </el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { updateRequest, getConfigs } from "@/api/setting";

export default {
  name: "InlineEditTable",
  filters: {
    statusFilter(status) {
      const statusMap = {
        可用: "success",
        待验证: "danger",
        过期: "info",
      };
      return statusMap[status];
    },
  },
  data() {
    return {
      list: null,
      listLoading: true,
      configVisible: false,
      temp: {
        parse_type:"weibo",
        headers: null,
        cookies: null,
        status: null,
      },
    };
  },
  created() {
    this.getList();
  },
  methods: {
    async getList() {
      this.listLoading = true;

      const { data } = await getConfigs();
      this.list = data.configs;
      this.listLoading = false;
    },
    editConfig(row) {
      // this.temp = row.fields;
      this.temp = {...row.fields}
      this.configVisible = true;
    },

    async updateConfig() {
      this.listLoading = true;
      this.temp.status = "待验证";
      const { data } = await updateRequest(this.temp);
      this.configVisible = false,

      this.$message({
          message: data.message,
          type: "info",
        });
      this.getList();
      this.listLoading = false;
    },
  },
};
</script>

<style scoped>
.edit-input {
  padding-right: 100px;
}
</style>
