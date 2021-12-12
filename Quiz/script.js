const startButton = document.getElementById("start=btn")
const nextButton = document.getElementById("next-btn")

const questioncontainerElement = doucment.getElementById("question-container")
const questionElement = doucment.getElementById('question')
const answerButtonElement = doucment.getElementById('answer-buttons')
let shffledQuestion, currentQuestionIndex;
let quizScore = 0;

startButton.addEventListener('click',startGame)
nextButton.addEventListener('click', ()=> {
    currentQuestionIndex++
    setNextQueston()
})

function startGame(){
    startButton.classList.add('hide')
    shffledQuestion = question.sort(()=> Math.randow() -0.5)
    currentQuestionIndex = 0;
    questioncontainerElement.classList.remove('hide')
    setNextQueston()
    quizScore=0
}

function setNextQueston(){
    resetState();
    showQuestion(shffledQuestion[currentQuestionIndex])
}

function showQuestion(question){
    questionElement.innerText= question.question;
    question.answers.forEach((answers)=>{
        const button = doucment.createElement('button')
        button.innerText= answer.text;
        button.classList.add('btn')
        if(answer.correct){
            button.data.correct = answer.correct
        }
        button.addEventListener('click',selectAnswer)
        answerButtonElement.appendChild(button)
    })
}

function resetState(){
    clearStatusClass(document.body)
    nextButton.classList.add('hide')
    while(answerButtonElement.firstChild){
        answerButtonElement.removeChild(answerButtonElement.firstChild)
    }
}

function selectAnswer(e){
    const selectedButton=e.target
    const correct = selectedButton.dataset.correct

    setStatusClass(doucment.body, correct)
    Array.from(answerButtonElement.children).forEach((button) =>{
        setStatusClass(button,button.dataset.correct)
    })
    if(shffledQuestion.length > currentQuestionIndex +1){
        nextButton.classList.remove('hide')
    }else{
        startButton.innerText="restart"
        startButton.classList.remove("hide")
    }
    if(selectedButton.dataset=correct){
        quizScore++
    }
    document.getElementById('reight-answers').innerText=quizScore
}

function setStatusClass(element, correct){
    clearStatusClass(element)
    if(correct){
        element.classList.add('correct')
    }
    else{
        element.classList.add('wrong')
    }
}

function clearStatusClass(element){
    element.classList.remove('corrent')
    element.classsList.remove('wrong')
}




const question = [
    {
        question : "Which one of these these is a JavaScript framework?",
        answers : [
            {text:'Python', correct: false},
            {text:'Django', correct: false},
            {text:'React', correct: true},
            {text:'Ecilpse', correct: false},
        ],
    },
    {
        question : "what is multiple of 43*8",
        answers : [
            {text:'234', correct: false},
            {text:'444', correct: false},
            {text:'344', correct: true},
            {text:'360', correct: false},
        ],
    },
]