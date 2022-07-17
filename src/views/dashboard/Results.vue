<template>
    <div class="container">
        <div class="columns is-multiline">
          
            <div class="column is-12">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Student Id</th>
                            <th>how do you evaluate the professor's technological mastery?</th>
                            <th>how do you evaluate the professor's teaching style?</th>
                            <th>Does the professor come to class on time?</th>
                            <th>How do you evaluate the interaction between the professor and the students?</th>
                            <th>How do you evaluate the professor's grading method?</th>
                            <th>Does the professor take periodic exams?</th>
                            <th>Anything dosent mention in questions</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="result in results" v-bind:key="result.id">
                            <td>{{ result.student_id }}</td>
                            <td>{{ result.q1 }}</td>
                            <td>{{ result.q2 }}</td>
                            <td>{{ result.q3 }}</td>
                            <td>{{ result.q4 }}</td>
                            <td>{{ result.q5 }}</td>
                            <td>{{ result.q6 }}</td>
                            <td>{{ result.q7 }}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>
<script>

import axios from 'axios'

export default {
    name: 'Results',
    data() {
        return {
            results: []
        }

    },
    mounted() {
        this.getResults()
    },
    methods: {
        async getResults() {
            this.$store.commit('setIsLoading', true)
            axios
                .get('/api/v1/results/')
                .then(response => {
                    this.results = response.data
                })
                .catch(error => {
                    console.log(error)
                })
            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>