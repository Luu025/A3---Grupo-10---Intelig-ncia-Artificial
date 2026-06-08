import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import pickle
import os

class EmailSpamDetector:
    def __init__(self, model_path='spam_model.pkl'):
        self.model_path = model_path
        self.model = None
        
        # Palavras-chave comuns em spam
        self.spam_keywords = [
            'urgente', 'clique aqui', 'ganhe dinheiro', 'oferta especial',
            'limitado', 'ação agora', 'prêmio', 'grátis', 'desconto',
            'confirmação', 'verificar', 'confirmar dados', 'atualizar',
            'click here', 'act now', 'limited time', 'special offer',
            'free money', 'congratulations', 'winner', 'claim'
        ]
    
    def train(self, emails, labels):
        """
        Treina o modelo com emails e rótulos (0=não spam, 1=spam)
        
        Args:
            emails: Lista de textos de emails
            labels: Lista de rótulos (0 ou 1)
        """
        # Criar pipeline com vetorizador TF-IDF e Naive Bayes
        self.model = Pipeline([
            ('tfidf', TfidfVectorizer(max_features=1000, stop_words=['a', 'the', 'o', 'a'])),
            ('clf', MultinomialNB())
        ])
        
        # Treinar o modelo
        self.model.fit(emails, labels)
        print("✓ Modelo treinado com sucesso!")
    
    def save_model(self):
        """Salva o modelo treinado em arquivo"""
        if self.model:
            with open(self.model_path, 'wb') as f:
                pickle.dump(self.model, f)
            print(f"✓ Modelo salvo em {self.model_path}")
    
    def load_model(self):
        """Carrega o modelo de um arquivo"""
        if os.path.exists(self.model_path):
            with open(self.model_path, 'rb') as f:
                self.model = pickle.load(f)
            print(f"✓ Modelo carregado de {self.model_path}")
            return True
        return False
    
    def predict(self, email_text):
        """
        Prediz se um email é spam ou não
        
        Args:
            email_text: Texto do email
            
        Returns:
            (prediction, confidence): 0=não spam, 1=spam; confiança da predição
        """
        if not self.model:
            return None, None
        
        # Converter para minúsculas
        email_text = email_text.lower()
        
        # Contar palavras-chave de spam
        spam_score = sum(1 for keyword in self.spam_keywords if keyword in email_text)
        
        # Usar o modelo treinado
        prediction = self.model.predict([email_text])[0]
        confidence = max(self.model.predict_proba([email_text])[0])
        
        # Se muitas palavras-chave de spam, aumentar confiança
        if spam_score >= 3:
            prediction = 1
            confidence = min(confidence + 0.2, 1.0)
        
        return prediction, confidence
    
    def classify_email(self, email_text):
        """
        Classifica um email e retorna resultado legível
        
        Args:
            email_text: Texto do email
            
        Returns:
            str: Resultado da classificação
        """
        prediction, confidence = self.predict(email_text)
        
        if prediction is None:
            return "Modelo não foi treinado ou carregado!"
        
        result = "SPAM" if prediction == 1 else "NÃO SPAM"
        confidence_percent = f"{confidence * 100:.2f}%"
        
        return f"{result} (confiança: {confidence_percent})"


# Exemplos de uso
if __name__ == "__main__":
    # Dados de treinamento (exemplos simples)
    training_emails = [
        # Emails legítimos (não-spam)
        "Olá, gostaria de agendar uma reunião para discutir o projeto.",
        "Relatório mensal disponível para download.",
        "Confirmação de pedido número 12345.",
        "Bem-vindo à nossa empresa, seu usuário foi criado com sucesso.",
        "Reunião agendada para segunda-feira às 10:00.",
        "Aqui está o documento que você solicitou.",
        "Sua conta foi atualizada com sucesso.",
        "Informações sobre benefícios dos funcionários.",
        "Feedback sobre o projeto entregue.",
        "Convite para a conferência anual.",
        
        # Emails de spam
        "CLIQUE AQUI AGORA! Ganhe dinheiro rápido!!!",
        "Você ganhou um prêmio! Verificar dados agora!",
        "Oferta especial: desconto limitado para hoje apenas!",
        "Ação urgente requerida! Confirme seus dados imediatamente!",
        "Parabéns! Você é o grande vencedor! Reivindicar prêmio agora!",
        "Dinheiro grátis! Clique aqui para receber seu bônus!",
        "Oferta exclusiva: 70% de desconto, tempo limitado!",
        "URGENTE: Atualizar informações bancárias agora!",
        "Click here to claim your FREE prize!",
        "Limited time offer - Act now! Don't miss out!",
    ]
    
    training_labels = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    
    # Criar detector
    detector = EmailSpamDetector()
    
    # Treinar modelo
    print("=" * 60)
    print("DETECTOR DE SPAM EM EMAILS")
    print("=" * 60)
    print("\nTreinando o modelo...")
    detector.train(training_emails, training_labels)
    detector.save_model()
    
    # Testar com novos emails
    print("\n" + "=" * 60)
    print("TESTANDO EMAILS")
    print("=" * 60)
    
    test_emails = [
        "Olá, você tem tempo para uma rápida reunião?",
        "CLIQUE AGORA! Ganhe R$ 10.000 GRÁTIS!!!",
        "Documento técnico do projeto anexado.",
        "Oferta urgente: desconto limitado de 80%!",
        "Seu pedido foi processado com sucesso."
    ]
    
    for i, email in enumerate(test_emails, 1):
        result = detector.classify_email(email)
        print(f"\nEmail {i}:")
        print(f"Mensagem: {email}")
        print(f"Resultado: {result}")
