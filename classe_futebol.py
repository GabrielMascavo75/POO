# Classe Base - Jogadores de Futebol Americano

class Jogador:
    def __init__(self, nome, camisa):
        self.nome = nome
        self.camisa = camisa
        self.em_jogo = True

    def entrou_em_campo(self):
        return f'{self.nome} entrou em campo!'
    
    def saiu_de_campo(self):
        self.em_jogo = False
        return f'{self.nome} saiu de campo.'
    
    def __str__(self):
        return f'{self.nome} - {'Em jogo' if self.em_jogo else 'No banco'}'

# Classe Derivadas - Tipos de jogadores
# Jogadores de Ataque

class Quarterback (Jogador):
    def lancar_bola(self, alvo):
        return f'{self.nome} lança a bola para {alvo}!'
    
class Runningback (Jogador):
    def correr_com_bola(self):
        return f'{self.nome} recebe a bola e avança as jardas!'
    
class Fullback (Jogador):
    def bloqueio_ativo(self):
        return f'{self.nome} corre e possui bloqueio mais forte na linha de ataque!'
    
class Widereceiver (Jogador):
    def receber_passe(self):
        return f'{self.nome} recebe agilmente passes longos!'
    
class Tightend (Jogador):
    def ataque_hibrido(self):
        return f'{self.nome} bloqueia o quarterback e recebe passe curto!'
    
class Offensivelineman(Jogador):
    def __init__(self, nome, camisa, posicao):
        super().__init__(nome, camisa)
        self.posicao = posicao #center, guard, tackle

    def proteger(self):
        return f'{self.nome} protege o quarterback com um bloqueio, enquanto passa a bola para o mesmo.'
    
#Jogadores de Defesa

class Defensivelineman(Jogador):
    def __init__(self, nome, camisa, posicao):
        super().__init__(nome, camisa)
        self.posicao = posicao #tackle ou end

    def bloquear_qb(self):
        return f'{self.nome} derruba o quarterback adversário e para as corridas!'
    
class Linebacker(Jogador):
    def defesa_hibrida(self):
        return f'{self.nome} cobre recebedores, para corridas e derruba quarterback!'
    
class Defensiveback(Jogador):
    def __init__(self, nome, camisa, posicao):
        super().__init__(nome, camisa)
        self.posicao = posicao #cornerback e safety

    def cobrir_receptor(self):
        return f'{self.nome} protege o recebedor!'
    
# Jogadores Especiais

class Specialteam(Jogador):
    def __init__(self, nome, camisa, posicao):
        super().__init__(nome, camisa)
        self.posicao = posicao # kicker, punter, long snapper, retornador

    def acao(self):
        if self.posicao == 'kicker':
            return f'{self.nome} chuta o field goal fazendo um extra point!'
        elif self.posicao == 'punter':
            return f'{self.nome} chuta a bola quando o time não consegue avançar as 10 jardas!'
        elif self.posicao == 'long snapper':
            return f'{self.nome} faz o lance perfeito de 7 a 15 jardas para o Punter!'
        elif self.posicao == 'retornador':
            return f'{self.nome} retorna o chute adversário e avança o máximo de campo possível!'
        else:
            return f'{self.nome} executa sua função em times especiais.'

# Classe de Herança Múltipla

class Widereceiveretornador(Widereceiver, Specialteam):
    def __init__(self, nome, camisa):
        Widereceiver.__init__(self, nome, camisa)
        Specialteam.__init__(self, nome, camisa, 'retornador')

    def __str__(self):
        return f'{super().__str__()} - Funções: Wide Reciver e Retornador'
    
if __name__ == '__main__':
    print("=== ATAQUE ===")
    qb = Quarterback("Tom Brady", 12)
    wr = Widereceiver("Jerry Rice", 80)
    rb = Runningback("Adrian Peterson", 28)

    print(qb)
    print(qb.lancar_bola(wr.nome))
    print(wr.receber_passe())
    print(rb.correr_com_bola())
    print()

    print("=== DEFESA ===")
    lb = Linebacker("Ray Lewis", 52)
    cb = Defensiveback("Deion Sanders", 21, "cornerback")
    de = Defensivelineman("J.J. Watt", 99, "end")

    print(lb)
    print(lb.defesa_hibrida())
    print(cb.cobrir_receptor())
    print(de.bloquear_qb())
    print()

    print("=== TIMES ESPECIAIS ===")
    kicker = Specialteam("Adam Vinatieri", 4, "kicker")
    print(kicker)
    print(kicker.acao())
    print()

    print("=== HERANÇA MÚLTIPLA (WR + Retornador) ===")
    devin = Widereceiveretornador("Devin Hester", 23)
    print(devin)
    print(devin.receber_passe())
    print(devin.acao())
    print()

    print("=== POLIMORFISMO ===")
    jogadores = [qb, wr, rb, lb, cb, kicker, devin]
    for jogador in jogadores:
        print(f"{jogador.nome}: {jogador.entrou_em_campo()}")