<template>
  <div class="w-full flex flex-col items-center">
    <form
      v-if="!showResults"
      id="searchForm"
      class="flex flex-col items-center w-full max-w-[400px]"
      role="search"
      aria-label="Formulário de busca de especialistas médicos"
      @submit.prevent="handleSubmit"
    >
      <div class="w-full mb-2">
        <input
          type="text"
          id="nome_completo"
          v-model="form.nome_completo"
          placeholder="Nome do Especialista"
          class="form-input-custom rounded-t-[1.5rem]"
        />
      </div>
      <div class="w-full mb-2">
        <select id="especialidade" v-model="form.especialidade" class="form-input-custom form-select-custom">
          <option value="" disabled selected>Especialidade Médica</option>
          <option value="cardiologia">Cardiologista</option>
          <option value="clinico-geral">Clínico Geral</option>
          <option value="ortopedia">Ortopedista</option>
          <option value="dermatologia">Dermatologista</option>
        </select>
      </div>
      <div class="w-full mb-2">
        <select id="cidade" v-model="form.cidade" class="form-input-custom form-select-custom">
          <option value="" disabled selected>Selecione a Cidade</option>
          <option value="salvador">Salvador</option>
          <option value="sao-paulo">São Paulo</option>
          <option value="rio-de-janeiro">Rio de Janeiro</option>
        </select>
      </div>
      <div class="w-full mb-2">
        <input
          id="id_date"
          ref="datepicker"
          v-model="form.data"
          placeholder="Data Desejada"
          class="form-input-custom"
        />
      </div>
      <div class="w-full mb-2">
        <select id="periodo" v-model="form.periodo" class="form-input-custom form-select-custom">
          <option value="" disabled selected>Período Desejado</option>
          <option value="manha">Manhã</option>
          <option value="tarde">Tarde</option>
          <option value="noite">Noite</option>
          <option value="madrugada">Madrugada</option>
        </select>
      </div>
      <div class="w-full mb-2">
        <select
          id="tipo_analise"
          v-model="form.tipo_analise"
          class="form-input-custom form-select-custom rounded-b-[1.5rem]"
        >
          <option value="" disabled selected>Tipo de Análise</option>
          <option value="preco">Preço</option>
          <option value="convenio">Convênio</option>
        </select>
      </div>
      <div class="w-full flex justify-center pt-4">
        <button type="submit" class="btn-enviar">Enviar</button>
      </div>
    </form>

    <section
      v-if="showResults && resultados.length > 0"
      class="w-full max-w-[400px] md:max-w-[500px] lg:max-w-[600px] xl:max-w-[800px]
             bg-white rounded-2xl shadow-xl p-4 sm:p-5 flex flex-col font-inter"
      aria-live="polite"
    >
      <div class="flex justify-between items-center mb-4">
        <h2 class="text-lg font-bold mago-text-blue">
          Resultados da Pesquisa
          <span class="font-normal text-base mago-text-blue">{{ currentIndex + 1 }} de {{ resultados.length }}</span>
        </h2>
        <button
          @click="resetSearch"
          class="btn-enviar !py-2 !px-4 !text-sm"
        >
          Recomeçar
        </button>
      </div>

      <div class="flex items-center justify-between gap-2">
        
        <button
          v-if="resultados.length > 1"
          @click="prevSlide" 
          :disabled="currentIndex === 0"
          class="w-10 h-10 flex-shrink-0 rounded-full flex items-center justify-center bg-dolfidocGray text-dolfidocBlue text-2xl font-bold transition-all hover:bg-gray-400 disabled:opacity-30 disabled:cursor-not-allowed mago-arrow-shadow"
          aria-label="Anterior"
        >
          ‹
        </button>
        <div v-else class="w-10 h-10 flex-shrink-0"></div>
        
        <div class="flex-grow text-left py-2 min-h-[420px] md:min-h-0 min-w-0 flex flex-col">
          
          <div class="flex-shrink-0 flex justify-center items-center mb-3">
            
            <img
              v-if="resultados[currentIndex].foto_url"
              :src="getApiFotoUrl(resultados[currentIndex].foto_url)"
              :alt="`Foto de ${resultados[currentIndex].nome}`"
              class="w-20 h-20 md:w-24 md:h-24 rounded-full object-cover border-2 mago-border-blue"
            />

            <div
              v-else
              class="w-20 h-20 md:w-24 md:h-24 bg-dolfidocGray rounded-full flex items-center justify-center !text-dolfidocBlue font-bold text-3xl md:text-4xl flex-shrink-0 border-2 mago-border-blue"
              aria-hidden="true"
            >
              {{ getInitials(resultados[currentIndex].nome) }}
            </div>
          </div>
          <div class="flex-shrink-0 text-center !text-dolfidocBlue mb-3"> 
            <h5 class="text-lg md:text-xl font-bold break-words mago-text-blue">
              {{ resultados[currentIndex].nome }}
            </h5>
            <p class="text-sm md:text-base font-medium text-text-light italic">
              CRM: {{ resultados[currentIndex].crm }}
            </p>
            <p class="text-sm md:text-base font-semibold mt-1">
              Especialidade: {{ resultados[currentIndex].especialidade }}
            </p>
          </div>

          <hr class="my-3 border-t border-dolfidocGray" />

          <div class="flex-grow flex flex-col items-start gap-4 text-sm md:text-base">
            
            <div class="space-y-1 text-text min-w-0">
              <p><strong>Empresa:</strong> {{ resultados[currentIndex].nome_fantasia || 'Não informado' }}</p>
              <p><strong>CNPJ:</strong> {{ resultados[currentIndex].cnpj || 'Não informado' }}</p>
              <p><strong>Contato:</strong> {{ resultados[currentIndex].telefone || 'Não informado' }}</p>
              <p><strong>Endereço:</strong> {{ formatarEndereco(resultados[currentIndex]) }}</p>
            </div>

            </div>

          <div 
            v-if="resultados[currentIndex].valores_consulta && resultados[currentIndex].valores_consulta.length > 0" 
            class="w-full mt-3 pt-3 border-t border-dolfidocGray"
          >
            <p class="text-text space-y-1 text-sm mb-2">
              <strong>Valor da Consulta:</strong>
            </p>
            <div class="mt-1 space-y-2">
              <div 
                v-for="(valor, index) in resultados[currentIndex].valores_consulta" 
                :key="index"
                class="w-fit text-dolfidocBlue border-2 mago-border-blue py-2 px-4 text-base font-bold rounded-lg shadow-lg text-center"
              >
                R$ {{ valor }}
              </div>
            </div>
          </div>
        </div>

        <button
          v-if="resultados.length > 1"
          @click="nextSlide"
          :disabled="currentIndex === resultados.length - 1"
          class="w-10 h-10 flex-shrink-0 rounded-full flex items-center justify-center bg-dolfidocGray text-dolfidocBlue text-2xl font-bold transition-all hover:bg-gray-400 disabled:opacity-30 disabled:cursor-not-allowed mago-arrow-shadow"
          aria-label="Próximo"
        >
          ›
        </button>
        <div v-else class="w-10 h-10 flex-shrink-0"></div>
      </div>
    </section>

    <div v-if="carregando" class="w-full text-center text-dolfidocBlue font-semibold p-8">
      Carregando resultados...
    </div>
    
    <div v-if="erro" class="w-full text-center text-error font-semibold p-8">
      {{ erro }}
    </div>

    <div
      v-if="showResults && resultados.length === 0 && !carregando && !erro"
      class="w-full bg-white rounded-2xl shadow-xl p-5 flex flex-col items-center text-center font-inter max-w-[400px] md:max-w-[500px] lg:max-w-[600px] xl:max-w-[800px]"
    >
      <p class="text-text-light mb-4">Nenhum resultado encontrado.</p>
      <button
        @click="resetSearch"
        class="btn-enviar !py-2 !px-4 !text-sm"
      >
        Recomeçar
      </button>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref, onMounted, nextTick } from 'vue'
import flatpickr from 'flatpickr'
import { Portuguese } from 'flatpickr/dist/l10n/pt.js'
import 'flatpickr/dist/flatpickr.min.css'
import api from '@/services/api' // Importa a instância do axios

// === INÍCIO DA CORREÇÃO DA FOTO ===
// 3. Helper para construir a URL completa da foto
const getApiFotoUrl = (path) => {
  // api.defaults.baseURL virá do seu 'services/api.js' 
  // (ex: 'http://localhost:8001/api/v1/')
  // O 'path' será 'cardiologistas/123/foto/'
  // O resultado é a URL completa para a tag <img>
  
  // Garante que não haja barras duplicadas
  const baseUrl = api.defaults.baseURL.endsWith('/') 
    ? api.defaults.baseURL.slice(0, -1) 
    : api.defaults.baseURL;
    
  const fotoPath = path.startsWith('/') ? path.slice(1) : path;
  
  return `${baseUrl}/${fotoPath}`;
}
// === FIM DA CORREÇÃO DA FOTO ===


// ==== Dados do formulário ====
const form = reactive({
  nome_completo: '',
  especialidade: '',
  cidade: '',
  data: '',
  periodo: '',
  tipo_analise: '',
})

const resultados = ref([])
const currentIndex = ref(0)
const carregando = ref(false)
const erro = ref(null)
const showResults = ref(false)
const datepicker = ref(null)

const toggleSideVisibility = (visible) => {
  const event = new CustomEvent('toggle-side', { detail: { visible } })
  window.dispatchEvent(event)
}

const getInitials = (name) => {
  if (!name || typeof name !== 'string') return '?'
  const parts = name.split(' ')
  if (parts.length === 1) return parts[0].substring(0, 2).toUpperCase()
  return (parts[0].substring(0, 1) + parts[parts.length - 1].substring(0, 1)).toUpperCase()
}

onMounted(async () => {
  await nextTick() 

  if (datepicker.value) {
    flatpickr(datepicker.value, {
      locale: Portuguese,
      dateFormat: 'd/m/Y',
      allowInput: true,
      disableMobile: true,
      position: 'below center',
      static: false,
      monthSelectorType: 'static',
      clickOpens: true,
      onOpen: () => {
        const calendar = document.querySelector('.flatpickr-calendar')
        if (calendar) calendar.style.zIndex = '9999'
      },
    })
  }

  document.addEventListener('click', e => {
    if (e.target.closest('.header__logo')) resetSearch()
  })
})


const handleSubmit = async () => {
  carregando.value = true
  erro.value = null

  try {
    const response = await api.get('cardiologistas/', {
      params: {
        nome_completo: form.nome_completo,
        especialidade: form.especialidade,
        cidade: form.cidade,
      },
    })

    let data = response.data

    // Se vier resposta paginada (tem count/next/results)
    if (data.results) {
      data = data.results
    }

    // Caso agrupado por CRM
    if (data.agrupado && data.medicos) {
      resultados.value = Object.values(data.medicos).flat()
    }
    // Caso lista simples
    else if (data.medicos) {
      resultados.value = data.medicos
    }
    // Caso a API devolva diretamente um array (edge case)
    else if (Array.isArray(data)) {
      resultados.value = data
    }
    // Caso não tenha nada
    else {
      resultados.value = []
    }

    console.log("🩺 Resultados normalizados:", resultados.value)

    currentIndex.value = 0
    showResults.value = true

    if (resultados.value.length > 0) {
      await nextTick()
      toggleSideVisibility(false)
    }

  } catch (e) {
    console.error("Erro ao buscar médicos:", e)
    erro.value = 'Erro ao buscar médicos. Verifique sua conexão ou tente novamente.'
  } finally {
    carregando.value = false
  }
}

const nextSlide = () => {
  if (currentIndex.value < resultados.value.length - 1) {
    currentIndex.value++
  }
}

const prevSlide = () => {
  if (currentIndex.value > 0) {
    currentIndex.value--
  }
}

const resetSearch = () => {
  showResults.value = false
  resultados.value = []
  currentIndex.value = 0
  Object.keys(form).forEach(k => (form[k] = ''))
  erro.value = null
  toggleSideVisibility(true)
}

const formatarEndereco = (medico) => {
  const partes = []
  if (medico.logradouro) partes.push(medico.logradouro)
  if (medico.numero) partes.push(medico.numero)
  if (medico.complemento) partes.push(medico.complemento)
  if (medico.cidade) partes.push(medico.cidade)
  if (medico.uf) partes.push(medico.uf)

  return partes.filter(p => p && String(p).toLowerCase() !== 'nan').join(', ') || 'Não informado'
}
</script>

<style scoped>
/* Estilos permanecem os mesmos */
.mago-text-blue {
  color: #2f3061 !important;
}
.mago-border-blue {
  border-color: #2f3061 !important;
}
.mago-arrow-shadow {
  box-shadow: 0 5px 12px rgba(0, 0, 0, 0.35) !important;
}
</style>