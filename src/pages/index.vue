<template>
  <div id="container">    
    <div class="top-offset"></div>

    <div id="card-display">
      <input 
        id="seed" type="text" v-model="seed_input"
        maxlength="8"
      />

      <div class="question" @click="toggle_show_answer">
        <p class="question"> 
          {{flashcards[index][0]}}
        </p>
        <p class="answer" >
          {{ displayed_answer }}
        </p>
      </div>

      
      <div class="buttons">
        <button class="arrow" @click="previous_card">
          ᐊ
        </button>

        <button 
          id="display-toggle"
          @click="toggle_show_answer"
        >
          <p v-show="!show_answer"> show </p>
          <p v-show="show_answer"> hide </p>
        </button>

        <button id="reset" @click="reset">
          ↺
        </button>

        <button class="arrow" @click="next_card">
          ᐅ
        </button>
      </div>

      <p id="card-no"> {{index+1}} / {{flashcards.length}} </p>
    </div>

    <div class="bottom-offset"></div>
  </div>
</template>

<script lang="ts">
import { ref, computed } from 'vue'
import { PRNG } from 'prng'
import clone from 'clone'

import shuffle from 'Shuffle'
import { defineComponent } from 'vue'
import RAW_FLASHCARDS from '@/assets/flashcards.json'
import pseudoRandom from 'pseudo-random';

console.log('FLASHCARDS', RAW_FLASHCARDS)

const scramble = (seed, arr) => {
  const spaced_seed = seed * (seed + 921) + 141721256
  // console.log('SCRAMBLE', seed, arr)
  const prng = pseudoRandom(spaced_seed)
  const arr_clone = clone(RAW_FLASHCARDS)
  const arr_shuffle = []

  while (arr_clone.length > 0) {
    const length = arr_clone.length
    const rand = prng.random()
    const index = Math.floor(rand*length)
    // console.log('REMOVED', arr_clone.length, rand, index)

    const removed_item = arr_clone.splice(index, 1)[0];
    arr_shuffle.push(removed_item)
  }  

  // console.log('SHUFFLE', arr_shuffle)
  // console.log('SCRAMBLE-END', seed, arr_shuffle.map(x => x[0]))
  return clone(arr_shuffle)
}

export default defineComponent({
  setup(props) {
    const self = this;
    const index = ref(0);
    const show_answer = ref(false);
    const seed_input = ref('')

    const flashcards = computed(() => {
      if (seed_input.value === '') { 
        return clone(RAW_FLASHCARDS) 
      }
      const seed = Number(seed_input.value)
      if (!Number.isInteger(seed)) { 
        return clone(RAW_FLASHCARDS)  
      }
      return scramble(seed, RAW_FLASHCARDS)
    });
    const toggle_show_answer = () => {
      show_answer.value = !show_answer.value;
    }

    const displayed_answer = computed(() => {
      if (show_answer.value) {
        // console.log('FLASHCARDS', flashcards.value, index)
        return flashcards.value[index.value][1]
      } else {
        return "██████████"
      }
    })

    const next_card = () => {
      if (index.value >= RAW_FLASHCARDS.length - 1) {
        return;
      }
      show_answer.value = false;
      index.value += 1;
    };
    const previous_card = () => {
      if (index.value <= 0) {
        return;
      }
      show_answer.value = false;
      index.value -= 1;
    };
    const reset = () => { 
      show_answer.value = false;
      index.value = 0 
    }

    return {
      flashcards, index, displayed_answer,
      toggle_show_answer, show_answer, seed_input,
      next_card, previous_card, reset
    };
  },
})
</script>

<style lang="scss" scoped>
*::selection {
  background-color: #FFF;  /* Set the background color for selected text */
  color: #222;              /* Set the text color for selected text */
}

@font-face {
  font-family: 'Open Sans';
  src: url('@/assets/fonts/OpenSans-Regular.ttf') format('ttf');
  /* You can specify multiple font formats (e.g., woff2, ttf) for better browser compatibility */
}

* {
  font-family: 'Open Sans';
}

div#container {
  margin: auto;
  display: flex;
  justify-content: center;
  flex-direction: column;
  height: 100vh;
  
  & > div.top-offset {
    flex-grow: 0.5;
  }
  & > div.bottom-offset {
    flex-grow: 1;
  }

  & div#card-display {
    // margin-left: 2rem;
    // margin-right: 2rem;
    flex-direction: column;
    text-align: center;
    flex-grow: 0;
    // padding-bottom: 10rem;

    & > div.question {
      padding-left: 0.5rem;
      padding-right: 0.5rem;
      background-color: #333;
      border-radius: 0.25rem;
      margin-bottom: 1rem;
      user-select: none;
      width: 22rem;

      display: flex;
      flex-direction: column;
      
      cursor: pointer;

      &:hover {
        background-color: #444;
      }
      &:active {
        background-color: #555;
      }

      & > p.question {
        font-size: 9rem;
        margin-top: -1rem;
      }

      & > p.answer {
        margin: auto;
        width: fit-content;
        margin-bottom: 1rem;
        margin-top: -1rem;
      }
    }

    & > input#seed {
      border: none;
      border-bottom: 2px solid #777;
      outline: none;
      // transition: border-color 0.3s ease-in-out;
      background-color: #111;
      margin-bottom: 0.5rem;
      width: 5rem;
      margin-left: auto;
      margin-right: auto;
      text-align: center;

      &::selection {
        background-color: #FFF;  /* Set the background color for selected text */
        color: #222;              /* Set the text color for selected text */
      }

      &:hover {
        border-color: #BBB;
      }
      &:active {
        border-color: #FFF;
      }
    }

    & > .buttons {
      display: flex;
      margin-top: 1rem;
      justify-content: space-between;
      width: 20rem;
      user-select: none;
      margin-left: auto;
      margin-right: auto;

      & > button.arrow {
        margin-left: 1rem;
        margin-right: 1rem;
        font-size: 2rem;
        user-select: none;
        color: #777;

        &:hover {
          color: #AAA;
        }
        &:active {
          color: #FFF;
        }
      }

      & > button:not(.arrow) {
        padding: 0.5rem;
        border: 1px solid #777;
        border-radius: 0.25rem;

        // margin: auto;
        &:hover {
          border-color: #AAA;
        }
        &:active {
          border-color: #FFF;
        }

        &#reset {
          width: 2.5rem;
        }
      }

      & > button#display-toggle {
        flex-grow: 1;
        margin-right: 0.5rem;
      }
    }

    & > p#card-no {
      width: fit-content;
      padding-top: 1rem;
      margin: auto;
    }
  }
}
</style> 