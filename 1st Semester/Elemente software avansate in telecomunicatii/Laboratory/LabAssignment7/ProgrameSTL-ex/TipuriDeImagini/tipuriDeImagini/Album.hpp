#ifndef _ALBUM_HPP
#define _ALBUM_HPP

#include "Bmp_16bpp.hpp"
#include "Bmp_256bpp.hpp"
#include "jpg.hpp"
#include "gif.hpp"
#include "tiff.hpp"
#include "Imagine.hpp"
#include <iostream>
#include <vector>
#include <algorithm>

enum Types {BMP_16BPP, BMP_256BPP, JPG, GIF, TIFF};

class Album
{
public:
	Album(void);
	~Album(void);

	void addImagine(Imagine*);
	void ShowImages(void);

	int GetPicsNo ( void ) const;
	int GetTotalSize ( void ) const;
	int GetPicsNo ( Types );
	Imagine* GetPicsByName ( std::string inName );
	void SortByName ( void );
	void SortBySize ( const bool down );
	void Compress ( void );

private:
	class NameFind
	{
	public:
		NameFind ( const std::string&);
		~NameFind ();

		bool operator () (const Imagine*);
	private:
		std::string mName;
	};

	class ByNameSort
	{
	public:
		ByNameSort(void);
		~ByNameSort(void);

		bool operator () (const Imagine*, const Imagine*);
	};

	class BySizeSort
	{
	public:
		BySizeSort(void);
		~BySizeSort(void);

		bool operator () (const Imagine*, const Imagine*);
	};

	class BySizeSortDown
	{
	public:
		BySizeSortDown(void);
		~BySizeSortDown(void);

		bool operator () (const Imagine*, const Imagine*);
	};

	std::vector<Imagine*> imgVec;
};
#endif //_ALBUM_HPP