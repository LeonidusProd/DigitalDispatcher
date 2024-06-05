<template>
  <select class="my-select"
          v-model="selectedOption"
          @change="this.$emit('selectChanged', this.selectedOption.pk)">
    <option v-for="option in options"
            v-bind:value="option">{{ option.name }}
    </option>
  </select>
</template>

<script>
export default {
  name: 'my-select',
  props: {
    options: [Array],
    placeholder: [String]
  },
  data() {
    return {
      selectedOption: null,
    }
  },
  methods: {}
}
</script>

<style scoped>
.my-select {
  display: block;
  width: 100%;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #212523;
  //-webkit-appearance: none;
  //-moz-appearance: none;
  //appearance: none;
  background-color: #fff;
  background-clip: padding-box;
  border: 2px solid #a9a89f;
  border-radius: 10px;
  margin-bottom: 10px;
}

.my-select:focus {
  color: #212523;
  background-color: #fff;
  border-color: #8bb6b1;
  outline: 0;
}
</style>