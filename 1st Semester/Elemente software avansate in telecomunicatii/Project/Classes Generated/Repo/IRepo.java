package Repo;

import java.util.*;

/**
 * 
 */
public interface IRepo extends UserRepo, DonationRepo {

    /**
     * @param T elem
     */
    public void add(void T elem);

    /**
     * @param id
     */
    public void remove(Long id);

    /**
     * @param id
     */
    public void update(Long id);

}