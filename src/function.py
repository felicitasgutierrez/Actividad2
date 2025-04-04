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

def determine_best_player(stats):
    """Determina el mejor jugador del partido."""
    best_player = max(stats.items(), key=lambda x: x[1]['total_points'])
    return best_player

def show_mvp_counts(stats):
    """Muestra la cantidad de MVPs por jugador."""
    print("\nCantidad de MVPs por jugador:")
    for player, data in stats.items():
        print(f"{player}: {data['mvp_count']} MVPs")

def simulate_games(rounds):
    """Simula el juego y calcula las estadísticas por ronda"""
    players = list(rounds[0].keys())                    
    stats = start_count (players)                        
    
    for i, round in enumerate(rounds, 1):              
        print(f"\n--- Ronda {i} ---")
        round_scores = {}                                
        
        for player in players:                          
            data = round[player]                       
            points = calculate_points_round(data)      
            round_scores[player] = points              
            sum_points (stats, player, data['kills'], data['assists'], data['deaths'], points)             
        mvp, points_mvp = define_mvp(round_scores)    
        stats[mvp]['mvp_count'] += 1                  
        print(f" MVP de la Ronda: {mvp} (Puntos: {points_mvp})")            
        show_ranking(stats)    
    best_player, best_stats = determine_best_player(stats)
    print(f"\n MEJOR JUGADOR DEL PARTIDO: {best_player} (Puntos Totales: {best_stats['total_points']})")
    show_mvp_counts(stats)  
    
    return stats