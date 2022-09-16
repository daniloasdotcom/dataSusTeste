library(microdatasus)

sim.es <- fetch_datasus(year_start = 2010, 
                        month_start = 1, 
                        year_end = 2020, 
                        month_end = 12, 
                        uf = "ES", 
                        information_system = "SIM-DO")

sim.es <- process_sim(sim.es)
print(typeof(sim.es$CAUSABAS))