<template>
  <div class="pusher">
    <div class="ui vertical masthead center aligned segment">
      <div class="ui container">
        <!--<div class="ui large secondary menu">-->
          <!--<a class="active item">Home</a>-->
        <!--</div>-->
      </div>
      <div class="ui text container">
        <h1 class="ui header">
          <img src="../assets/logo.png">
        </h1>
        <h2>Get tweets by twitter handle</h2>
        <form method="get" @submit.prevent="checkForm">
          <div v-if="errors.length">
            <ul>
              <div class="ui visible red message" v-for="error in errors">
                <p>{{ error }}</p>
              </div>
            </ul>
          </div>
          <div class="ui big icon input" v-bind:class="{ loading: isLoading}">
            <input type="text" placeholder="Enter a twitter handle" v-model="keyword">
            <i class="search icon"></i>
          </div>
          <button class="ui huge primary button">Search <i class="right arrow icon"></i></button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  import './Home.css'

  export default {
    data() {
      return {
        errors: [],
        keyword: null,
        tweets: [],
        isLoading: false,
      }
    },
    methods: {
      getTweets() {
        this.tweets = this.getTweetsFromBackend()
      },
      getTweetsFromBackend() {
        const keyword = this.keyword;
        const path = `${process.env.API_URL}/tweets/?user=${keyword}`;
        let self = this;
        axios.get(path)
          .then(response => {
            this.tweets = response.data
          })
          .catch(error => {
            this.errors.push('Error.');
          })
          .then(function () {
            self.isLoading = false;
          });
      },
      checkForm() {
        this.errors = [];
        this.isLoading = true;
        if (this.keyword) {
          this.getTweets();
          return true;
        }

        this.errors = [];

        if (!this.keyword) {
          this.errors.push('Twitter handle is required.');
        }
        this.isLoading = false;
      },
    },
    created() {
    }
  }
</script>
