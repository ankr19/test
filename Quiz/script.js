const startButton = document.getElementById('start-btn')
const questionContainerElement = document.getElementById('question-container')
const questionElement = document.getElementById('question')
const answerButtonElement = document.getElementById('answer-buttons')
const nextButton = document.getElementById('next-btn')
let shuffledQuestion, currectQuestionIndex

startButton.addEventListener('click', startGame)
nextButton.addEventListener('click',() => {
    currectQuestionIndex++;
    setNextQuestion()
})

function startGame(){
    console.log("started")
    startButton.classList.add('hide');
    shuffledQuestion = questions.sort(()=> Math.random() - .5)
    currectQuestionIndex = 0;
    questionContainerElement.classList.remove('hide')
    setNextQuestion();
}

function setNextQuestion() {
    resetState()
    showQuestion(shuffledQuestion[currectQuestionIndex])
}

function showQuestion(question) {
    questionElement.innerText = question.question
    question.answers.forEach(answer => {
        const button = document.createElement('button')
        button.innerText= answer.text
        button.classList.add('btn')
        if(answer.correct)
        {
            button.dataset.correct = answer.correct
        }
        button.addEventListener('click', selectAnswer)
        answerButtonElement.appendChild(button)
    });
}

function resetState() {
    nextButton.classList.add('hide')
    while(answerButtonElement.firstChild)
    {
        answerButtonElement.removeChild(answerButtonElement.firstChild)
    }
}

function selectAnswer(e) {
    const selectedButton = e.target
    const correct = selectedButton.dataset.correct
    setStatusClass(document.body, correct)
    Array.from(answerButtonElement.children).forEach(button =>{
        setStatusClass(button, button.dataset.correct)
    })
    if(shuffledQuestion.length > currectQuestionIndex + 1){
        nextButton.classList.remove('hide')
    }
    else{
        startButton.innerText = 'Restart'
        startButton.classList.remove('hide')
    }
}

function setStatusClass(element, correct)
{
    clearStatusClass(element)
    if(correct){
        element.classList.add('correct')
    }
    else{
        element.classList.add('wrong')
    }
}

function clearStatusClass(element) {
    element.classList.remove('correct')
    element.classList.remove('wrong')
}

// const questions = [
//     {
//         question: ' what is r.a.m?',
//         answers: [
//             { text: 'random access memory', correct:true },
//             { text: 'random arthimetic memorial', correct:false }
//         ]
//     }
// ]

const questions = [
    //question 1
            {
              question: 'Which crop is sown in the most important area in India?',
              answers: [ 
                        { text: '(A) Rice', correct: true },
                        { text: '(B) Wheat', correct: false },
                        { text: '(C) Sugarcane', correct: false },
                        { text: '(D) Maize', correct: false }
                      ]
            },
            // question 2
            {
                question: 'Eritrea, which became the 182nd member of the United Nations in 1993, is on the continent of',
              answers: [ 
                        { text:'(A) Asia', correct: false },
                        { text: '(B) Africa', correct: true },
                        { text: '(C) Europe', correct: false},
                        { text: '(D) Australia', correct: false } 
                    ]
            },
            // question 3
            {
                question: 'Which of the subsequent personalities gave ‘The Laws of Heredity?',
                answers: [
                    { text:'(A) Robert Hook', correct:false },
                    { text:'(B) G.J. Mendel', correct:true },
                    { text:'(C) Darwin', correct:false },
                    { text:'(D) Harvey', correct:false }
                ]
            },

            // question 4
            {
                question: 'Garampani sanctuary is found at',
                answers: [
                    { text:'(A) Junagarh, Gujarat', correct:false },
                    { text:'(B) Diphu, Assam', correct: true },
                    { text:'(C) Kohima, Nagaland', correct: false },
                    { text:'(D) Gangtok, Sikkim', correct: false }
                ]
            },
            //question 5
           {
            question:'Who is understood as “The Saint of Gutters”?',
            answers: [
                { text:'(A) Baba Amte', correct: false },
                { text:'(B) Teresa', correct: true },
                { text:'(C) Anna Hazare', correct: false },
                { text:'(D) None of those', correct: false }
            ]
           },
           // question 6:
           {
               question:'that of the subsequent disciplines is Nobel prize awarded?',
               answers: [
                { text:'(A) Physics and Chemistry', correct:false },
                { text:'(B) Physiology or Medicine', correct:false },
                { text:'(C) Literature, Peace and Economics', correct:false },
                { text:'(D) All of the above', correct:true }
               ]
           },
           // question 7
           {
               question:'Grand Central Terminal, Park Avenue, NY is that the world?',
               answers: [
                { text:'(A) largest railroad station', correct:true },
                { text:'(B) highest railroad station', correct:false },
                { text:'(C) longest railroad station', correct:false },
                { text:'(D) None of the above', correct:false }
                
               ]
           },
           // question 8
           {
               question:'Name the one that was also referred to as Deshbandhu.',
               answers: [
                { text:'(A) S. Radhakrishnan', correct:false },
                { text:'(B) G.K. Gokhale', correct:false },
                { text:'(C) Chittaranjan Das', correct:true},
                { text:'(D) Madan Mohan Malviya', correct:false }
               ]
           },
           // question 9
           {
               question:'FFC stands for',
               answers: [
                { text:'(A) Foreign Finance Corporation', correct:false },
                { text:'(B) Film Finance Corporation', correct:true },
                { text:'(C) Federation of Football Council', correct:false },
                { text:'(D) None of the above', correct:false }
               ] 
           },
           // question 10
           {
               question:"Which of the subsequent national parks is not listed during a UNESCO World Heritage site?",
               answers:[
                   { text:'(A) Kaziranga', correct:false },
                   { text:'(B) Keoladeo', correct: false },
                   { text:'(C) Sundarbans', correct:false },
                   { text:'(D) Kanha', correct: true }
               ]
           }
]