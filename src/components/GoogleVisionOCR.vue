<template>
    <div class="google-vision-ocr">
      <Button label="Reconnaître le texte (Google Vision)" @click="recognizeText" :loading="loading" />
      <ProgressBar v-if="progress > 0" :value="progress" />
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import Button from 'primevue/button';
  import ProgressBar from 'primevue/progressbar';
  
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
      // Simuler une progression pour l'exemple
      const interval = setInterval(() => {
        progress.value += 10;
        if (progress.value >= 100) clearInterval(interval);
      }, 200);
  
      // Appel à l'API Google Cloud Vision
      const response = await fetch('https://vision.googleapis.com/v1/images:annotate?key=YOUR_API_KEY', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          requests: [
            {
              image: {
                content: props.imageData.split(',')[1] // Enlever le préfixe "data:image/...;base64,"
              },
              features: [
                {
                  type: 'DOCUMENT_TEXT_DETECTION'
                }
              ]
            }
          ]
        })
      });
  
      const result = await response.json();
      const recognizedText = result.responses[0].fullTextAnnotation.text;
  
      emit('text-recognized', recognizedText);
    } catch (error) {
      console.error('Erreur lors de la reconnaissance du texte:', error);
    } finally {
      loading.value = false;
      progress.value = 100;
    }
  };
  </script>