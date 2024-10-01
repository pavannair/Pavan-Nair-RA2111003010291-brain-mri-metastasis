{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c73695f6-8f87-4871-9527-47457abe9e43",
   "metadata": {},
   "outputs": [],
   "source": [
    "from fastapi import FastAPI\n",
    "\n",
    "app = FastAPI()\n",
    "\n",
    "@app.get(\"/\")\n",
    "def read_root():\n",
    "    return {\"Hello\": \"World\"}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "24fa23dc-a277-4761-b715-dfe9dc1a1b8c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
