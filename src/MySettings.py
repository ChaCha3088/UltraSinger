class MySettings:
    def __init__(self, input_file_path="", output_file_path=""):
        self.APP_VERSION = "0.0.8"

        self.create_midi = False
        self.create_plot = False
        self.create_audio_chunks = False
        self.hyphenation = True
        self.use_separated_vocal = True
        self.create_karaoke = True

        self.input_file_path = input_file_path
        self.output_file_path = output_file_path
        self.processing_audio_path = ""

        self.language = None
        self.format_version = "1.0.0"

        # Transcribe
        self.audio_chunk_folder_name = "audio-chunks"

        # Whisper
        self.transcriber = "whisper"  # whisper
        self.whisper_model = "medium"  # Multilingual model tiny|base|small|medium|large-v1|large-v2
        # English-only model tiny.en|base.en|small.en|medium.en
        self.whisper_align_model = None   # Model for other languages from huggingface.co e.g -> "gigant/romanian-wav2vec2"
        self.whisper_batch_size = 16   # reduce if low on GPU mem
        self.whisper_compute_type = None   # change to "int8" if low on GPU mem (may reduce accuracy)

        # Pitch
        self.crepe_model_capacity = "full"  # tiny|small|medium|large|full
        self.crepe_step_size = 10 # in miliseconds

        # Device
        self.pytorch_device = 'cuda'  # cpu|cuda
        self.tensorflow_device = 'cuda'  # cpu|cuda
        self.force_cpu = False
        self.force_whisper_cpu = False
        self.force_crepe_cpu = False