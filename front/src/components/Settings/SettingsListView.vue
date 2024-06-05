<template>
  <h5 v-if="this.elementsList.length === 0">{{ this.emptyHeader }}</h5>

  <div v-else class="cards">
    <div class="list custom-scroll">

      <SettingsListCard v-for="element in this.elementsList"
                        :pk="element.pk"
                        :name="element.name"
                        :model-name="modelName"
                        @deleteElement="$emit('deleteElement')">
      </SettingsListCard>
    </div>
  </div>
</template>

<script>

import SettingsListCard from "@/components/Settings/SettingsListCard.vue";

export default {
  components: {SettingsListCard},
  props: {
    emptyHeader: [String],
    elementsList: [Array],
    modelName: [String],
  }
}
</script>

<style scoped>
.cards {
  height: 185px;
}

.list {
  display: flex;
  flex-direction: column;
  overflow-y: auto;
  padding-right: 3px;
  border-radius: 12px;
  height: 185px;
}

.custom-scroll::-webkit-scrollbar {
  width: 5px;
}

.custom-scroll::-webkit-scrollbar-track {
  background: rgb(169, 168, 159);
  border-radius: 6px;
}

.custom-scroll::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 6px;
}

.custom-scroll::-webkit-scrollbar-thumb:hover {
  background: #555;
}
</style>