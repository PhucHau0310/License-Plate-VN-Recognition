'use client';
import React, { useState } from 'react';

export default function Home() {
    const [selectedFile, setSelectedFile] = useState<File | null>(null);
    const [previewUrl, setPreviewUrl] = useState<string>('');
    const [isLoading, setIsLoading] = useState<boolean>(false);
    const [resultImage, setResultImage] = useState<string>('');
    const [licensePlate, setLicensePlate] = useState<string>('');

    const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const file = e.target.files?.[0];
        if (file) {
            setSelectedFile(file);
            setPreviewUrl(URL.createObjectURL(file));
        }
    };

    const handleUpload = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        if (!selectedFile) return;

        setIsLoading(true);

        const formData = new FormData();
        formData.append('file', selectedFile);

        try {
            const response = await fetch('http://localhost:8000/detect', {
                method: 'POST',
                body: formData,
            });

            const data = await response.json();

            setLicensePlate(data.plate_text);
            setResultImage(data.image_base64);
        } catch (error) {
            alert('Error uploading file. Please try again.');
            setLicensePlate('');
            setResultImage('');
            setPreviewUrl('');
            setSelectedFile(null);
            setIsLoading(false);
            console.error('Upload failed:', error);
        } finally {
            setIsLoading(false);
        }
    };

    const handleChooseAnother = () => {
        setSelectedFile(null);
        setPreviewUrl('');
        setResultImage('');
        setLicensePlate('');
    };

    return (
        <div className="max-w-[1360px] mx-auto px-4 py-8">
            <h1 className="text-center font-semibold text-4xl text-white">
                License Plate Recognition
            </h1>

            <div className="flex flex-row justify-between mt-14 gap-20">
                {/* Upload Panel */}
                <div className="w-1/2 border border-white rounded-lg p-4">
                    <h2 className="text-center font-semibold text-2xl text-white">
                        Upload an image
                    </h2>
                    <p className="text-center text-gray-400">
                        Upload an image of a car with a visible license plate.
                    </p>

                    <form
                        className="flex flex-col items-center justify-center mt-4"
                        onSubmit={handleUpload}
                        encType="multipart/form-data"
                    >
                        <input
                            type="file"
                            name="image"
                            accept="image/*"
                            className="mb-4 p-2 border border-gray-300 rounded"
                            onChange={handleFileChange}
                        />

                        {previewUrl ? (
                            <img
                                src={previewUrl}
                                alt="Preview"
                                className="w-2/3 h-60 mb-4 rounded"
                            />
                        ) : (
                            <div className="w-2/3 h-60 bg-gray-800 rounded flex items-center justify-center mb-4">
                                <p>
                                    <span className="text-gray-500">
                                        No image selected
                                    </span>
                                </p>
                            </div>
                        )}

                        <div className="flex gap-4">
                            <button
                                type="submit"
                                className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 disabled:opacity-50"
                                disabled={!selectedFile || isLoading}
                            >
                                {isLoading ? 'Uploading...' : 'Upload'}
                            </button>

                            {selectedFile && (
                                <button
                                    type="button"
                                    onClick={handleChooseAnother}
                                    className="bg-gray-500 text-white px-4 py-2 rounded hover:bg-gray-600"
                                >
                                    Choose Another
                                </button>
                            )}
                        </div>
                    </form>
                </div>

                {/* Result Panel */}
                <div className="w-1/2 border border-white rounded-lg p-4">
                    <h2 className="text-center font-semibold text-2xl text-white">
                        Results
                    </h2>
                    <p className="text-center text-gray-400">
                        The results of the license plate recognition will be
                        displayed here.
                    </p>

                    <div className="mt-4 flex flex-col items-center">
                        {resultImage && (
                            <img
                                src={`data:image/png;base64,${resultImage}`}
                                alt="Result"
                                className="w-2/3 h-60 mb-4 rounded"
                            />
                        )}
                        {licensePlate && (
                            <>
                                <h3 className="text-center font-semibold text-xl text-white">
                                    License Plate Number
                                </h3>
                                <p className="text-center text-gray-400 font-bold">
                                    {licensePlate}
                                </p>
                            </>
                        )}
                    </div>
                </div>
            </div>
        </div>
    );
}
