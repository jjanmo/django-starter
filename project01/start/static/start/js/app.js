const $options = document.querySelectorAll('input[name="option"]');
const $inputContainer = document.querySelector('.input_container');

const handleChange = (e) => {
    const option = e.target.value;
    if(option === '자동'){
        $inputContainer.classList.add('hidden');
    } else {
        $inputContainer.classList.remove('hidden');
    }
}

$options.forEach($option => $option.addEventListener('change', handleChange));