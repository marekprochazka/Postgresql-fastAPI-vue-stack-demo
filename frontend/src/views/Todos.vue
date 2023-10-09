<script setup lang="ts">
  import useApi from "@/composables/useApi";
  import {ref} from "vue";
  const loading = ref(false);
  const api = useApi();

  const todos = ref([]);
  todos.value = await api.get('/todos/list');

  console.log(todos);
</script>

<template>
  <div class="todos" v-if="todos">
      <div v-for="todo in todos">
        {{todo}}
      </div>
  </div>
</template>