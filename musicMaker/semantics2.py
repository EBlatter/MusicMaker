#Import the library
from midiutil.MidiFile import MIDIFile

class MusicSemantics:

	def __init__(self, trackName = 'MusicMakerSong'):
		self.trackName = trackName
		# Create the MIDIFile Object with 1 track
		self.file = MIDIFile(1)

		# Tracks are numbered from zero. Times are measured in beats.
		self.track = 0
		self.time = 0

		# Add track name and tempo.
		self.file.addTrackName(self.track,self.time,trackName)
		self.file.addTempo(self.track,self.time,240)

		#start pitch and volume that everything else will be relative to
		self.pitch = 75
		self.maxVol = 0

		self.vowels = ['a','e','i','o','u','y']

	
	def addNote(self, note):
		# Add a note. addNote expects the following information:
		maxVowels = 1
		for subnote in note.vowels:
			maxSubnoteVowels = self.findMaxVowels(subnote)
			if maxSubnoteVowels > maxVowels:
				maxVowels = maxSubnoteVowels
		
		track = 0
		channel = 0
		pitch = self.pitch - note.pitch
		duration = 1 * maxVowels
		volume = 100.0*(note.volume/self.maxVol)

		# Now add the note.
		self.file.addNote(track,channel,pitch,self.time,duration,volume)

		self.time += duration

	def findMaxVowels(self, subnote):
		maxLength = 0
		for vowel in self.vowels:
			count = subnote.count(vowel)
			if maxLength < count:
				maxLength = count
		return maxLength

	def findMaxVolume(self, notes):
		for note in notes:
			if float(note.volume) > self.maxVol:
				self.maxVol = float(note.volume)

	def createSong(self, notes):
		self.findMaxVolume(notes)
		for note in notes:
			self.addNote(note)

		# And write it to disk.
		binfile = open(self.trackName+'.mid', 'wb')
		self.file.writeFile(binfile)

		binfile.close()