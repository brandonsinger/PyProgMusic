# -*- coding: utf-8 -*-

#http://python.dzone.com/articles/sound-synthesis-numpy
#http://www.sengpielaudio.com/calculator-notenames.htm
#http://en.wikipedia.org/wiki/Scientific_pitch_notation
#http://www.howmusicworks.org/301/Chords-and-Harmony/Interval-Sizes
#http://www.howmusicworks.org/502/Meter-and-Rhythm/Note-Symbols
#http://www.wolframalpha.com/input/?i=What+frequencies+can+a+violin+sound%3F
#http://www.easyeartraining.com/2010/03/23/percussion-frequencies-part-1-drums/
#http://www.zytrax.com/tech/audio/audio.html
#http://lateblt.tripod.com/synths.htm
#http://www.ams.org/samplings/feature-column/fcarc-synthesizer
#
#http://codingmess.blogspot.com/2008/07/how-to-make-simple-wav-file-with-python.html
#http://soledadpenades.com/2009/10/29/fastest-way-to-generate-wav-files-in-python-using-the-wave-module/
#http://kenschutte.com/python-audio-demo


#import?


#drum sounds
#kick drums: 80-130-150Hz
#Snares: 120-250Hz
#Floor Toms: 60-80-110Hz
#Regular Toms: 100-500-600Hz +
#kick drum: 114Hz
#snare drum: 217Hz
#Floor Tom 4: 65Hz
#Tom 3: 87Hz
#Tom 2: 128Hz
#Top 1: 150Hz


import numpy as N
import wave







class PyProgMusic(object):
    notes = {
        "C 0": 16.352,
        "C# 0": 17.324,
        "Db 0": 17.324,
        "D 0": 18.354,
        "D# 0": 19.445,
        "Eb 0": 19.445,
        "E 0": 20.602,
        "F 0": 21.827,
        "F# 0": 23.125,
        "Gb 0": 23.125,
        "G 0": 24.500,
        "G# 0": 25.957,
        "Ab 0": 25.957,
        "A 0": 27.500,
        "A# 0": 29.135,
        "Bb 0": 29.135,
        "B 0": 30.868,

        "C 1": 32.703,
        "C# 1": 34.648,
        "Db 1": 34.648,
        "D 1": 36.708,
        "D# 1": 38.891,
        "Eb 1": 38.891,
        "E 1": 41.203,
        "F 1": 43.654,
        "F# 1": 46.249,
        "Gb 1": 46.249,
        "G 1": 48.999,
        "G# 1": 51.913,
        "Ab 1": 51.913,
        "A 1": 55.000,
        "A# 1": 58.270,
        "Bb 1": 58.270,
        "B 1": 61.735,

        "C 2": 65.406,
        "C# 2": 69.296,
        "Db 2": 69.296,
        "D 2": 73.416,
        "D# 2": 77.782,
        "Eb 2": 77.782,
        "E 2": 82.407,
        "F 2": 87.307,
        "F# 2": 92.499,
        "Gb 2": 92.499,
        "G 2": 97.999,
        "G# 2": 103.83,
        "Ab 2": 103.83,
        "A 2": 110.00,
        "A# 2": 116.54,
        "Bb 2": 116.54,
        "B 2": 123.47,

        "C 3": 130.81,
        "C# 3": 138.59,
        "Db 3": 138.59,
        "D 3": 146.83,
        "D# 3": 155.56,
        "Eb 3": 155.56,
        "E 3": 164.81,
        "F 3": 174.61,
        "F# 3": 185.00,
        "Gb 3": 185.00,
        "G 3": 196.00,
        "G# 3": 207.65,
        "Ab 3": 207.65,
        "A 3": 220.00,
        "A# 3": 233.08,
        "Bb 3": 233.08,
        "B 3": 246.94,

        "C 4": 261.63,
        "C# 4": 277.18,
        "Db 4": 277.18,
        "D 4": 293.66,
        "D# 4": 311.13,
        "Eb 4": 311.13,
        "E 4": 329.63,
        "F 4": 349.23,
        "F# 4": 369.99,
        "Gb 4": 369.99,
        "G 4": 392.00,
        "G# 4": 415.30,
        "Ab 4": 415.30,
        "A 4": 440.00,
        "A# 4": 466.16,
        "Bb 4": 466.16,
        "B 4": 493.88,

        "C 5": 523.25,
        "C# 5": 554.37,
        "Db 5": 554.37,
        "D 5": 587.33,
        "D# 5": 622.25,
        "Eb 5": 622.25,
        "E 5": 659.26,
        "F 5": 698.46,
        "F# 5": 739.99,
        "Gb 5": 739.99,
        "G 5": 783.99,
        "G# 5": 830.61,
        "Ab 5": 830.61,
        "A 5": 880.00,
        "A# 5": 932.33,
        "Bb 5": 932.33,
        "B 5": 987.77,

        "C 6": 1046.5,
        "C# 6": 1108.7,
        "Db 6": 1108.7,
        "D 6": 1174.7,
        "D# 6": 1244.5,
        "Eb 6": 1244.5,
        "E 6": 1318.5,
        "F 6": 1396.9,
        "F# 6": 1480.0,
        "Gb 6": 1480.0,
        "G 6": 1568.0,
        "G# 6": 1661.2,
        "Ab 6": 1661.2,
        "A 6": 1760.0,
        "A# 6": 1864.7,
        "Bb 6": 1864.7,
        "B 6": 1975.5,

        "C 7": 2093.0,
        "C# 7": 2217.5,
        "Db 7": 2217.5,
        "D 7": 2349.3,
        "D# 7": 2489.0,
        "Eb 7": 2489.0,
        "E 7": 2637.0,
        "F 7": 2793.8,
        "F# 7": 2960.0,
        "Gb 7": 2960.0,
        "G 7": 3136.0,
        "G# 7": 3322.4,
        "Ab 7": 3322.4,
        "A 7": 3520.0,
        "A# 7": 3729.3,
        "Bb 7": 3729.3,
        "B 7": 3951.1,

        "C 8": 4186.0,
        "C# 8": 4434.9,
        "Db 8": 4434.9,
        "D 8": 4698.6,
        "D# 8": 4978.0,
        "Eb 8": 4978.0,
        "E 8": 5274.0,
        "F 8": 5587.7,
        "F# 8": 5919.9,
        "Gb 8": 5919.9,
        "G 8": 6271.9,
        "G# 8": 6644.9,
        "Ab 8": 6644.9,
        "A 8": 7040.0,
        "A# 8": 7458.6,
        "Bb 8": 7458.6,
        "B 8": 7902.1,

        "C 9": 8372.0,
        "C# 9": 8869.8,
        "Db 9": 8869.8,
        "D 9": 9397.3,
        "D# 9": 9956.1,
        "Eb 9": 9956.1,
        "E 9": 10548.1,
        "F 9": 11175.3,
        "F# 9": 11839.8,
        "Gb 9": 11839.8,
        "G 9": 12543.9,
        "G# 9": 13289.8,
        "Ab 9": 13289.8,
        "A 9": 14080.0,
        "A# 9": 14917.2,
        "Bb 9": 14917.2,
        "B 9": 15804.3,

        "C 10": 16744.0,
        "C# 10": 17739.7,
        "Db 10": 17739.7,
        "D 10": 18794.5,
        "D# 10": 19912.1,
        "Eb 10": 19912.1,
        "E 10": 21096.2,
        "F 10": 22350.6,
        "F# 10": 23679.6,
        "Gb 10": 23679.6,
        "G 10": 25087.7,
        "G# 10": 26579.5,
        "Ab 10": 26579.5,
        "A 10": 28160.0,
        "A# 10": 29834.5,
        "Bb 10": 29834.5,
        "B 10": 31608.5,
        }

    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate #16000, 22050, 32000, 44056, 44100(CD quality)
        self.qpm = 120 #quarter notes per minute
        self.channel_data = []

    def add_note(self, instrument, note, time):
        #time:
        #4 = whole note
        #2 = half note
        #1 = quarter note
        #.5 = 1/16 note
        #.25 = 1/32 note

        frequency = self.notes[note] # Hz
        duration = (60.0/self.qpm) * time #seconds
        samples = duration * self.sample_rate
        period = self.sample_rate / float(frequency) # in sample points
        volume = 16384 #half volume
        signal = instrument.create_note(frequency, duration, samples, period, volume);
       
        self.channel_data.append(signal)

    def write_out(self):
        signal = N.concatenate(self.channel_data, axis=0)
        ssignal = ''.join((wave.struct.pack('h', item) for item in signal)) # transform to binary
       
        file = wave.open('test.wav', 'wb')
        file.setparams((1, 2, self.sample_rate, 44100*4, 'NONE', 'noncompressed'))       
        file.writeframes(ssignal)
        file.close()

    def play(self):
        self.write_out()
        print "Playing music"

        import pyglet
        music = pyglet.resource.media("test.wav")
        player = pyglet.media.Player()
        player.queue(music)
        player.play()
        while player.playing:
            pyglet.clock.tick(30)


    def view(self):
        signal = N.concatenate(self.channel_data, axis=0)

        import matplotlib.pyplot as plt
        plt.plot(signal)
        plt.ylabel('some numbers')
        plt.show()

class Instrument(object):
    def create_note(self, frequency, duration, samples, period, volume):
        #http://www.ams.org/samplings/feature-column/fcarc-synthesizer
        #=A * sin(2π * f * t + p)
        #=A * sin(2π / T * t + p)
        #=A sin(2π * fc * t + I * sin(2π * fm * t))
        # A=amplitude
        # f=1/T
        # T=time for one period
        # t=?time
        # p=phase shift
        # loadness controled by A
        # timbre controled by I
        #fc=carrier frequency
        #fm=modulating frequency
        A = volume
        I = 5
        T = period
        fc = 1/T
        fm = 1/(T/2)
        t = N.arange(samples, dtype=N.float) #creates an array 'samples' big (1,2,3,4....samples)

        A *= self.A(samples)
        I = self.I(samples)
        
        signal = A * N.sin(2*N.pi * fc * t + I * N.sin(2*N.pi * fm * t))

            
        #//signal = N.resize(ydata, (samples,))
            
        
        return signal

    def _create_envelope(self, samples, actions):
        #types: line, exponential, logorithmic
        # ?: [type:?, length:(in amount or percent), start_value, stop_value]

        e = N.empty(samples, N.float)        
        position = 0

        for action in actions:
            if action['length'].endswith("%"):
                l = round(int(action['length'][:-1]) / 100.0 * samples)
            if position+l > samples:
                l = samples - position

            #print "Length: %s" % (l,)
            if action['type'] == 'line':
                e[position:position+l] = N.linspace(action['start_value'], action['stop_value'], l)
                #print "line %s:%s start:%s stop:%s" % (position, position+l, action['start_value'], action['stop_value'])
            elif action['type'] == 'exp':
                print "Base: %s" % (action['base'],)
                e[position:position+l] = action['base'] ** (N.arange(l, dtype=N.float)-action['pos'])


            position += l
                
        return e


class Tone(Instrument):
    def __init__(self):
        pass    
    
    def A(self, samples):
        #Controls loudnes
        return 1

    def fm(self, fc):
        #modulating frequency
        return fc
    
    def I(self, samples):
        #controls timbre
        return 0

class Bla(Instrument):
    def __init__(self):
        pass
    
    def A(self, samples):
        #Controls loudness
        A = N.empty(samples, N.float)

        top = int(samples * .05)

        A[:top] = N.linspace(0, 1, top)
        A[top:] = N.linspace(1, 0, samples-top)
        return A

    def fm(self, fc):
        return fc
        
    def I(self, samples):
        #controls timbre
        return self._create_envelope(samples, [{'type':'line', 'length':'100%', 'start_value':6, 'stop_value':0}])

class Brass(Instrument):
    def A(self, samples):
        return self._create_envelope(samples, [
                {'type':'line', 'length':'5%', 'start_value':0, 'stop_value':1},
                {'type':'line', 'length':'10%', 'start_value':1, 'stop_value':.9},
                {'type':'line', 'length':'80%', 'start_value':.9, 'stop_value':.8},
                {'type':'line', 'length':'5%', 'start_value':.8, 'stop_value':0},
                ])

    def fm(self, fc):
        return fc

    def I(self, samples):
        return self._create_envelope(samples, [
                {'type':'line', 'length':'5%', 'start_value':0, 'stop_value':2},
                {'type':'line', 'length':'10%', 'start_value':2, 'stop_value':1.9},
                {'type':'line', 'length':'80%', 'start_value':1.9, 'stop_value':1.8},
                {'type':'line', 'length':'5%', 'start_value':1.8, 'stop_value':0},
                ])

class Bell(Instrument):
    def A(self, samples):
        return self._create_envelope(samples, [
                {'type':'exp', 'length':'100%', 'base':.99999, 'pos':0}
                ])

    def fm(self, fc):
        return fc * 1.618 #golden ratio

    def I(self, samples):
        return self._create_envelope(samples, [
                {'type':'exp', 'length':'100%', 'base':.9999, 'pos':50}
                ])
    
    
if __name__ == "__main__":
    music = PyProgMusic()

    i = Bell()

    
    #http://www.music-scores.com/midi.php?sheetmusic=Xmas_Jingle_Bells_very_easy_piano
    
    music.add_note(i, "E 4", 1)
    music.add_note(i, "E 4", 1)
    music.add_note(i, "E 4", 2)

    """
    music.add_note(i, "E 4", 1)
    music.add_note(i, "E 4", 1)
    music.add_note(i, "E 4", 2)
    
    music.add_note(i, "E 4", 1)
    music.add_note(i, "G 4", 1)
    music.add_note(i, "C 4", 1.5)
    music.add_note(i, "D 4", .5)

    music.add_note(i, "E 4", 4)


    music.add_note(i, "F 4", 1)
    music.add_note(i, "F 4", 1)
    music.add_note(i, "F 4", 1.5)
    music.add_note(i, "F 4", .5)

    music.add_note(i, "F 4", 1)
    music.add_note(i, "E 4", 1)
    music.add_note(i, "E 4", 1)
    music.add_note(i, "E 4", .5)
    music.add_note(i, "E 4", .5)

    music.add_note(i, "E 4", 1)
    music.add_note(i, "D 4", 1)
    music.add_note(i, "D 4", 1)
    music.add_note(i, "E 4", 1)

    music.add_note(i, "D 4", 2)
    music.add_note(i, "G 4", 2)

    music.add_note(i, "E 4", 1)
    music.add_note(i, "E 4", 1)
    music.add_note(i, "E 4", 2)

    music.add_note(i, "E 4", 1)
    music.add_note(i, "E 4", 1)
    music.add_note(i, "E 4", 2)

    music.add_note(i, "E 4", 1)
    music.add_note(i, "G 4", 1)
    music.add_note(i, "C 4", 1.5)
    music.add_note(i, "D 4", .5)

    music.add_note(i, "E 4", 4)

    music.add_note(i, "F 4", 1)
    music.add_note(i, "F 4", 1)
    music.add_note(i, "F 4", 1)
    music.add_note(i, "F 4", 1)

    music.add_note(i, "F 4", 1)
    music.add_note(i, "E 4", 1)
    music.add_note(i, "E 4", 1)
    music.add_note(i, "E 4", .5)
    music.add_note(i, "E 4", .5)

    music.add_note(i, "G 4", 1)
    music.add_note(i, "G 4", 1)
    music.add_note(i, "F 4", 1)
    music.add_note(i, "D 4", 1)

    music.add_note(i, "C 4", 4)"""

    music.play()
