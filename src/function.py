# Inicializar 
def start_count(players):
    """Crea un diccionario con las estadísticas base para cada jugador."""
    
    stats = {}
    for player in players:
        stats[player] = {
            'kills': 0,
            'assists': 0,
            'deaths': 0,
            'mvp_count': 0,
            'total_points': 0
            }
    return stats

def calculate_points_round(data_player):
    """cuenta el puntaje de cada jugador para la ronda."""
    kills = data_player['kills']
    assists = data_player['assists']
    deaths = -1 if data_player['deaths'] else 0
    
    return kills * 3 + assists * 1 + deaths

def sum_points (stats, player, kills, assists, deaths, points):
    """actualiza el diccionario de estadisticas y puntajes."""
    stats[player]['kills'] += kills
    stats[player]['assists'] += assists
    stats[player]['deaths'] += (1 if deaths else 0)
    stats[player]['total_points'] += points

def define_mvp(round_scores):                          
    """Determinar mejor jugador de la ronda"""
    return max(round_scores.items(), key=lambda x: x[1])     

def  show_ranking(stats):
    """Ordena a los jugadores por total_points y muestra una tabla."""
    print("\nRanking Acumulado:")
    print("Jugador   | Kills | Asistencias | Muertes | MVPs | Puntos")
    print("-" * 50)
    sorted_players = sorted(stats.items(), key=lambda x: x[1]['total_points'], reverse=True)
    for player, data in sorted_players:
        print(f"{player.ljust(8)} | {str(data['kills']).ljust(5)} | {str(data['assists']).ljust(11)} | {str(data['deaths']).ljust(7)} | {str(data['mvp_count']).ljust(4)} | {data['total_points']}")
     
def simulate_games(rounds):
    """Simula el juego y calcula las estadísticas por ronda"""
    players = list(rounds[0].keys())                    #hago una lista de jugadores
    stats = start_count (players)                       #invoco a la función que me va a ir calculando los puntujes por ronda 
    
    for i, round in enumerate(rounds, 1):              #itero cada una de las rondas
        print(f"\n--- Ronda {i} ---")
        round_scores = {}                              #inicializo el diccionario q me va a guardar jugador/puntaje  
        
        for player in players:                         #itero por jugador en la ronda i 
            data = round[player]                       #data guarda en un diccionario los valores en la ronda i del jugador player
            points = calculate_points_round(data)      #calcula el puntaje del jugador player en la ronda i
            round_scores[player] = points              #guardo el puntaje que obtuvo el jugador player en la ronda i, es un dicc donde  las claves son nombres de jugadores y los valores son sus puntajes en esa ronda
            sum_points (stats, player, data['kills'], data['assists'], data['deaths'], points) #invoco la función que me va a ir actualizando el diccionario start
            
        mvp, points_mvp = define_mvp(round_scores)    #Esto es para calcular el mejor jugador del partido, la función me devuelve una tupla (player, points).
        stats[mvp]['mvp_count'] += 1                  # cuanta las veces que un jugador salio mvp
        print(f" MVP de la Ronda: {mvp} (Puntos: {points_mvp})")             #imprime el mvp y su puntaje
        
        show_ranking(stats)      
    
    return stats