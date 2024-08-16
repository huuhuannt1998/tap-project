import subprocess

def check_model(nusmv_model):
    with open('model.smv', 'w') as file:
        file.write(nusmv_model)
    
    nusmv_executable = r"C:\Program Files\NuSMV\2.5.4\bin\NuSMV.exe" 
    
    result = subprocess.run([nusmv_executable, 'model.smv'], capture_output=True, text=True)
    
    return result.stdout


nusmv_model = """
MODULE main
VAR
  door : {locked, unlocked};
  thermostat : 0..30;
  light : {on, off};
  presence : boolean;

ASSIGN
  init(door) := locked;
  init(thermostat) := 20;
  init(light) := off;
  init(presence) := FALSE;

  next(door) := case
    presence & (door = locked) : {locked, unlocked};
    !presence : locked;
    TRUE : door;
    esac;

  next(thermostat) := case
    thermostat < 30 : thermostat + 1;
    thermostat = 30 : thermostat;
    TRUE : thermostat;
    esac;

  next(light) := case
    presence & (light = off) : on;
    !presence : off;
    TRUE : light;
    esac;

  next(presence) := {TRUE, FALSE};

LTLSPEC G (!presence -> F door = locked)  -- Always, if presence is true, eventually the door will be locked
LTLSPEC G (thermostat <= 25) -- Always    , the thermostat is less than or equal to 25
LTLSPEC G (presence -> F light = on)      -- Always, if presence is true, eventually the light will be on
"""

# Run model checking
result = check_model(nusmv_model)
print(result)
