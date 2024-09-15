<template>
    <div class="easy-ocr">
      <Button label="Reconnaître le texte (EasyOCR)" @click="recognizeText" :loading="loading" />
      <ProgressBar v-if="progress > 0" :value="progress" />
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import Button from 'primevue/button';
  import ProgressBar from 'primevue/progressbar';
  import axios from 'axios';
  
  const props = defineProps({
    imageData: {
      type: String,
      required: true
    }
  });
  
  const emit = defineEmits(['text-recognized']);
  
  const loading = ref(false);
  const progress = ref(0);
  
  const recognizeText = async () => {
    loading.value = true;
    progress.value = 0;
  
    try {
      const response = await axios.post('http://localhost:5000/ocr', {
        image: