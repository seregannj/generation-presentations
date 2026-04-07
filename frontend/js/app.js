// frontend/js/app.js
// Конфигурация API
const API_URL = 'http://localhost:8000/api';  // Заменить на реальный URL при деплое

// Элементы DOM
const form = document.getElementById('reportForm');
const loading = document.getElementById('loading');
const result = document.getElementById('result');
const error = document.getElementById('error');
const generateBtn = document.getElementById('generateBtn');

let currentText = '';
let currentRequest = null;

// Обработка отправки формы
form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const topic = document.getElementById('topic').value;
    const style = document.getElementById('style').value;
    const wordCount = parseInt(document.getElementById('wordCount').value);
    
    currentRequest = { topic, style, word_count: wordCount };
    
    // UI состояние загрузки
    form.style.display = 'none';
    loading.style.display = 'block';
    result.style.display = 'none';
    error.style.display = 'none';
    generateBtn.disabled = true;
    
    try {
        // Сначала получаем текст для предпросмотра
        const response = await fetch(`${API_URL}/generate/text`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(currentRequest)
        });
        
        if (!response.ok) {
            const err = await response.json();
            throw new Error(err.detail || 'Ошибка сервера');
        }
        
        const data = await response.json();
        currentText = data.content;
        
        // Показываем результат
        document.getElementById('resultContent').textContent = data.content;
        document.getElementById('wordCountDisplay').textContent = `${data.word_count} слов`;
        
        loading.style.display = 'none';
        result.style.display = 'block';
        
    } catch (err) {
        loading.style.display = 'none';
        error.style.display = 'block';
        document.getElementById('errorText').textContent = err.message;
        console.error('Error:', err);
    } finally {
        generateBtn.disabled = false;
    }
});

// Копирование текста
function copyText() {
    navigator.clipboard.writeText(currentText).then(() => {
        showToast('📋 Текст скопирован!');
    });
}

// Скачивание DOCX
async function downloadDocx() {
    if (!currentRequest) return;
    
    const btn = document.querySelector('.btn-success');
    btn.textContent = '⏳ Генерация...';
    btn.disabled = true;
    
    try {
        const response = await fetch(`${API_URL}/generate/docx`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(currentRequest)
        });
        
        if (!response.ok) throw new Error('Ошибка генерации файла');
        
        // Скачиваем файл
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        
        // Формируем имя файла
        const safeTopic = currentRequest.topic.slice(0, 30).replace(/\s+/g, '_');
        a.download = `doclad_${safeTopic}.docx`;
        
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
        a.remove();
        
        showToast('✅ Файл скачан!');
        
    } catch (err) {
        showToast('❌ Ошибка: ' + err.message);
    } finally {
        btn.textContent = '⬇️ Скачать DOCX';
        btn.disabled = false;
    }
}

// Сброс формы
function resetForm() {
    form.style.display = 'block';
    error.style.display = 'none';
    result.style.display = 'none';
    document.getElementById('topic').value = '';
}

// Toast уведомление
function showToast(message) {
    const toast = document.getElementById('toast');
    toast.textContent = message;
    toast.style.display = 'block';
    setTimeout(() => {
        toast.style.display = 'none';
    }, 3000);
}
