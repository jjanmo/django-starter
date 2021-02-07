const $options = document.querySelectorAll('input[name="option"]');
const $form = document.querySelector('.form');
const $autoButton = document.querySelector('.auto_button');

const handleChange = (e) => {
    const option = e.target.value;
    if(option === '자동'){
        $form.classList.add('hidden');
        $autoButton.classList.remove('hidden');
    } else {
        $form.classList.remove('hidden');
        $autoButton.classList.add('hidden');
    }
}

$options.forEach($option => $option.addEventListener('change', handleChange));