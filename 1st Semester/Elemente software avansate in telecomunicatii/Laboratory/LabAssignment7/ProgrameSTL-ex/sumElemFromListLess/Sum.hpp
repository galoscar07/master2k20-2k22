#ifndef _SUM_HPP
#define _SUM_HPP

class Sum
{
public:
	Sum(void);
	Sum(int);
	~Sum(void);

	void operator()(int x);
	int result() const;

private:
	int mRes;
};
#endif //_SUM_HPP