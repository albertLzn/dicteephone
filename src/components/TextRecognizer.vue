<template>
    <div class="text-recognizer">
      <Button label="Reconnaître le texte" @click="recognizeText" :loading="loading" />
      <ProgressBar v-if="progress > 0" :value="progress" />
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import Button from 'primevue/button';
  import ProgressBar from 'primevue/progressbar';
  import * as Tesseract from 'tesseract.js';
  
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
      const worker = await Tesseract.createWorker('fra', 1, {
        logger: m => {
          if (m.status === 'recognizing text') {
            progress.value = m.progress * 100;
          }
        }
      });
  
      const { data: { text } } = await worker.recognize(props.imageData);
      await worker.terminate();
  
      emit('text-recognized', text);
    } catch (error) {
      console.error('Erreur lors de la reconnaissance du texte:', error);
    } finally {
      loading.value = false;
    }
  };
  </script>