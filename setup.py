from setuptools import setup

setup(
    name="magic123",
    packages=[
        "nerf",
    ],
    install_requires=[
        "filelock",
        "Pillow",
        "torch",
        "fire",
        "humanize",
        "requests",
        "tqdm",
        "matplotlib",
        "scikit-image",
        "scipy",
        "numpy",
        "blobfile",
        "clip @ git+https://github.com/openai/CLIP.git",
    ],
    author="OpenAI",
)
