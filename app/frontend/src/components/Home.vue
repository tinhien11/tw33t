<template>
  <div>
    <p>Home page</p>

    <form id="app" method="post" @submit.prevent="checkForm">
      <div v-if="errors.length">
        <b>Please correct the following error(s):</b>
        <ul>
          <li v-for="error in errors">{{ error }}</li>
        </ul>
      </div>

      <p>
        <label for="name">Name</label>
        <input type="text" name="name" id="name" v-model="name">
      </p>

      <p>
        <input type="submit" value="Submit">
      </p>
    </form>

    <div>
      {{tweets}}
    </div>

  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    data() {
      return {
        errors: [],
        name: null,
        tweets: []
      }
    },
    methods: {
      getTweets() {
        this.tweets = this.getTweetsFromBackend()
      },
      getTweetsFromBackend() {
        const username = this.name;
        const path = `${process.env.API_URL}/tweets/?user=${username}`
        axios.get(path)
          .then(response => {
            this.tweets = response.data
          })
          .catch(error => {
            this.errors.push('Error.');
          })
      },
      checkForm() {
        if (this.name) {
          this.getTweets()
          return true;
        }

        this.errors = [];

        if (!this.name) {
          this.errors.push('Name required.');
        }
      },
    },
    created() {
    }
  }
</script>
